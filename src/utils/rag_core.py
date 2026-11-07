"""FAQ RAG core: chunk -> embed (local) -> Qdrant (in-memory) -> answer (Ollama).

Importing this module loads every markdown file under FAQ_DIR once: read, chunk, embed, upsert.
Changes to the files are picked up on the next start.
All logging goes to stderr: the MCP server uses stdout as its protocol channel.
"""

import json
import logging
import re
import sys
import uuid
import ollama

from fastembed import TextEmbedding
from logging import Logger, StreamHandler
from pathlib import Path
from qdrant_client import QdrantClient, models
from re import Pattern
from typing import Any, Dict, List, LiteralString, TextIO
from uuid import UUID

# --- Config: every environment variable is read and validated in utils/__init__.py ---
from utils import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EMBED_MODEL,
    FAQ_DIR,
    MIN_SCORE,
    OLLAMA_MODEL,
    OLLAMA_TIMEOUT,
    OLLAMA_URL,
    TEMPERATURE,
    TOP_K_DEFAULT,
)

COLLECTION = "faqs"

# Fixed namespace: same file name + same chunk index => same chunk id, everywhere.
NAMESPACE: UUID = uuid.UUID(hex="6f1c7e0a-5b1d-4c53-9a53-3d5f2b8c9e10")

# --- Logging (stderr only) ---
log: Logger = logging.getLogger(name="rag")
log.setLevel(level=logging.INFO)
log.propagate = False
if not log.handlers:
    _h: StreamHandler[TextIO | Any] = logging.StreamHandler(sys.stderr)
    _h.setFormatter(
        fmt=logging.Formatter(
            fmt="%(asctime)s %(message)s",
            datefmt="%H:%M:%S",
        )
    )
    log.addHandler(hdlr=_h)

# --- Ollama (answer generation), local embeddings, in-memory Qdrant ---
client: Any = ollama.Client(
    host=OLLAMA_URL,
    timeout=OLLAMA_TIMEOUT,
)
_embedder: Any = TextEmbedding(model_name=EMBED_MODEL)
_DIM: int = len(next(iter(_embedder.embed(["dimension probe"]))))
_qdrant: Any = QdrantClient(":memory:")


def _check_ollama() -> None:
    """Warn (never crash) at startup if Ollama or the model is not available yet."""
    try:
        names: set[Any] = {m.model for m in client.list().models}
    except Exception as e:
        log.warning(
            msg=f"[warn] cannot reach Ollama at {OLLAMA_URL} ({e}). Answers will fail until it is up."
        )
        return
    if not any(n == OLLAMA_MODEL or n.split(":")[0] == OLLAMA_MODEL for n in names):
        log.warning(
            msg=f"[warn] model '{OLLAMA_MODEL}' is not pulled on {OLLAMA_URL}. Run: ollama pull {OLLAMA_MODEL}"
        )
    else:
        log.info(msg=f"ollama ok: {OLLAMA_MODEL} at {OLLAMA_URL}")


# ---------------- Chunking and ids ----------------
_ENTRY_START: Pattern[str] = re.compile(
    r"(?m)^(?=Q:|## )"
)  # a line starting "Q:" or "## " begins a FAQ entry


def _split_windows(
    text: str,
    size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP,
) -> List[str]:
    """Fixed windows of `size` characters, stepping by size - overlap."""
    step: int = max(1, size - overlap)
    chunks, i = [], 0
    while True:
        chunks.append(text[i : i + size])
        if i + size >= len(text):
            return chunks
        i += step


def _chunk_text(text: str) -> List[str]:
    """One chunk per FAQ entry, i.e. 'Q: ... A: ...' or '## question' plus its answer.

    The '# Title' line is not an entry and is dropped. An entry longer than CHUNK_SIZE is split
    into overlapping windows. A file with no entries at all falls back to fixed windows.
    """
    text: str = text.strip()
    if not text:
        return []
    if not _ENTRY_START.search(text):
        return _split_windows(text)
    parts: list[str | Any] = [p.strip() for p in _ENTRY_START.split(text) if p.strip()]
    if parts and "\n" not in parts[0] and parts[0].startswith("# "):
        parts: list[str | Any] = parts[1:]  # bare title line
    chunks: List[str] = []
    for part in parts:
        chunks.extend(_split_windows(text=part) if len(part) > CHUNK_SIZE else [part])
    return chunks


def _chunk_id(
    filename: str,
    index: int,
) -> str:
    return str(
        uuid.uuid5(
            namespace=NAMESPACE,
            name=f"{filename}:{index}",
        )
    )


# ---------------- Embeddings ----------------
def _embed_texts(texts: List[str]) -> List[List[float]]:
    return [v.tolist() for v in _embedder.embed(texts)]


def _embed_query(q: str) -> List[float]:
    return next(iter(_embedder.query_embed(q))).tolist()


# ---------------- Load: read -> chunk -> embed -> upsert (once) ----------------
def load_faqs() -> None:
    faq_dir: Path = FAQ_DIR
    if not faq_dir.is_dir():
        raise RuntimeError(f"FAQ_DIR does not exist: {faq_dir}")
    _qdrant.create_collection(
        COLLECTION,
        vectors_config=models.VectorParams(
            size=_DIM,
            distance=models.Distance.COSINE,
        ),
    )

    ids: List[str] = []
    texts: List[str] = []
    payloads: List[dict] = []
    files: list[Path] = sorted(faq_dir.glob(pattern="*.md"))
    for path in files:
        for i, chunk in enumerate(_chunk_text(text=path.read_text(encoding="utf-8"))):
            cid: str = _chunk_id(
                filename=path.name,
                index=i,
            )
            ids.append(cid)
            texts.append(chunk)
            payloads.append(
                {
                    "source": path.name,
                    "chunk_index": i,
                    "text": chunk,
                }
            )
            log.info(msg=f"[load] {path.name}#{i} {cid[:8]}")

    if texts:
        vectors: List[List[float]] = _embed_texts(texts)
        _qdrant.upsert(
            COLLECTION,
            points=[
                models.PointStruct(
                    id=cid,
                    vector=vec,
                    payload=p,
                )
                for cid, vec, p in zip(ids, vectors, payloads)
            ],
        )
    log.info(msg=f"loaded {len(texts)} chunks from {len(files)} files")


# ---------------- Answering ----------------
# What the user sees when the FAQs have nothing relevant (no sources are returned with it)
NOT_FOUND = "I couldn't find any information about that in the FAQs. Please try rephrasing your question."

# Only questions that look compound pay for the extra model call below.
_COMPOUND_REGEX: Pattern[str] = re.compile(
    r"\b(and|also|plus|then|as well as|along with)\b|[,;&]|\?\s*\S", re.I
)
_SPLIT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "questions": {
            "type": "array",
            "items": {
                "type": "string",
            },
        },
    },
    "required": ["questions"],
}


# Stored answers are cut to this many characters in the rewrite prompt (enough to resolve "it"/"that")
_HISTORY_ANSWER_CHARS = 500


def _format_history(history: List[Dict[str, str]]) -> str:
    lines: list[str] = []
    for turn in history:
        lines.append(f"User: {str(turn.get('question', '')).strip()}")
        lines.append(f"Assistant: {str(turn.get('answer', '')).strip()[:_HISTORY_ANSWER_CHARS]}")
    return "\n".join(lines)


def _split_question(
    q: str,
    history: List[Dict[str, str]] | None = None,
) -> List[str]:
    """Turn the user's message into standalone questions, one per topic.

    One embedding of "how to request PTO and reset my password" lands between the two topics and
    retrieves neither well, so each part is searched on its own. With a conversation history, a follow-up
    such as "and for contractors?" is also rewritten so it makes sense without the earlier turns.
    Returns [q] for a simple question without history, or if the model call fails."""
    if not history and not _COMPOUND_REGEX.search(q):
        return [q]
    try:
        if history:
            system: str = (
                "Rewrite the user's latest message into the separate, self-contained questions it contains. "
                "Use the earlier conversation only to resolve references such as 'it', 'that' or 'what about X?', "
                "so each question can be understood on its own. "
                "If the latest message is already self-contained or about a new topic, keep it unchanged and do not add "
                "anything from the conversation. If it contains several topics, return one question per topic. "
                "Never answer the questions. Return at most 4."
            )
            content: str = f"Conversation so far:\n{_format_history(history)}\n\nLatest message: {q}"
        else:
            system = (
                "Split the user's message into the separate, self-contained questions it contains, "
                "keeping the user's wording. If it contains only one question, return it unchanged. "
                "Never answer the questions. Return at most 4."
            )
            content = q
        resp = client.chat(
            model=OLLAMA_MODEL,
            options={
                "temperature": TEMPERATURE,
            },
            format=_SPLIT_SCHEMA,
            messages=[
                {
                    "role": "system",
                    "content": system,
                },
                {
                    "role": "user",
                    "content": content,
                },
            ],
        )
        parts: list[str] = [
            p.strip()
            for p in json.loads(s=resp.message.content)["questions"]
            if isinstance(p, str)
        ]
        return [p for p in parts if p][:4] or [q]
    except Exception as e:
        log.warning(
            msg=f"[warn] could not split the question ({e}); searching it as is"
        )
        return [q]


def _generate_answer(
    context: str,
    question: str,
) -> str:
    resp = client.chat(
        model=OLLAMA_MODEL,
        options={
            "temperature": TEMPERATURE,
        },
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer the question using ONLY the provided context. "
                    "Start with the direct answer, with no preamble such as 'According to the context'. "
                    "Be concise and include only what the question asks. "
                    "If the question has several parts, answer the parts the context covers and, for each part it does not cover, "
                    'write: "I couldn\'t find information about <that topic> in the FAQs." '
                    "Never mention documents, files or sources: they are shown to the user separately. "
                    "Format the reply as Markdown: use **bold** for key facts and a short bullet list "
                    "when there are several points, and do not add headings to short answers. "
                    f"If the context does not contain the answer at all, reply with exactly this sentence and nothing else: {NOT_FOUND}"
                ),
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}",
            },
        ],
    )
    return (resp.message.content or "").strip()


def ask_faq_core(
    question: str,
    top_k: int = TOP_K_DEFAULT,
    history: List[Dict[str, str]] | None = None,
) -> Dict[str, object]:
    q: str = (question or "").strip()
    if not q:
        raise ValueError("question is required")

    # top_k chunks for each sub-question; a chunk found by several of them is kept once
    questions: List[str] = _split_question(q, history=history)
    if len(questions) > 1 or questions != [q]:
        log.info(msg=f"[split] {questions}")
    # With history, the user's message may be a follow-up that means nothing alone: answer the rewrite
    standalone: str = " ".join(questions) if history else q
    hits, seen = [], set()
    for sub in questions:
        for h in _qdrant.query_points(
            COLLECTION,
            query=_embed_query(q=sub),
            limit=top_k if top_k > 0 and top_k <= 10 else TOP_K_DEFAULT,
            score_threshold=MIN_SCORE,
            with_payload=True,
        ).points:
            if h.id not in seen:
                seen.add(h.id)
                hits.append(h)
    if not hits:  # nothing scored above MIN_SCORE: skip the model call entirely
        empty: bool = _qdrant.count(COLLECTION).count == 0
        return {
            "answer": "No FAQ content is loaded." if empty else NOT_FOUND,
            "sources": [],
        }

    sources: List[str] = []
    for h in hits:
        if h.payload["source"] not in sources:
            sources.append(h.payload["source"])

    # No filenames in the context: the model cannot repeat what it never sees
    context: LiteralString = "\n\n---\n\n".join(h.payload["text"] for h in hits)
    answer: str = _generate_answer(
        context,
        question=standalone,
    )
    if answer.strip() == NOT_FOUND:
        sources: List[str] = []  # nothing relevant was found, so do not cite files
    return {
        "answer": answer,
        "sources": sources,
    }


# Load everything at import time (the MCP server imports this module)
_check_ollama()
load_faqs()

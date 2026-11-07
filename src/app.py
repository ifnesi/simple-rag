"""Flask backend. It never touches the vector DB: every question goes through the MCP server."""

import asyncio
import json
import logging
import re
import threading
import time
from collections import OrderedDict, deque
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
from mcp import ClientSession
from logging import Logger
from mcp.client.streamable_http import streamable_http_client
from typing import Any, Literal, LiteralString

# Settings come from utils/__init__.py (read from the environment and validated there)
from utils import CHAT_HISTORY_TURNS, MCP_URL, TOP_K_DEFAULT

app: Any = Flask(
    __name__,
    static_folder="frontend",
    static_url_path="",
)
log: Logger = logging.getLogger(name="web")
DOCS_DIR: Path = Path(__file__).parent / "docs"  # copied into the image by the Dockerfile


# ---------------- Chat memory ----------------
# The browser sends a session_id; the last CHAT_HISTORY_TURNS question/answer pairs of each session are
# kept in this process (lost on restart, not shared between workers) and sent to the MCP tool.
SESSION_TTL_SECONDS = 3600
MAX_SESSIONS = 500
_SESSION_ID = re.compile(r"^[A-Za-z0-9_-]{8,64}$")
_sessions: "OrderedDict[str, tuple[float, deque]]" = OrderedDict()
_sessions_lock = threading.Lock()


def _valid_session(session_id: Any) -> str | None:
    return session_id if isinstance(session_id, str) and _SESSION_ID.match(session_id) else None


def _get_history(session_id: str | None) -> list[dict]:
    if not session_id or CHAT_HISTORY_TURNS == 0:
        return []
    with _sessions_lock:
        entry = _sessions.get(session_id)
        if not entry or time.time() - entry[0] > SESSION_TTL_SECONDS:
            _sessions.pop(session_id, None)
            return []
        return list(entry[1])


def _remember(session_id: str | None, question: str, result: dict) -> None:
    # An answer without sources is the "couldn't find" message: it would only pollute the history
    if not session_id or CHAT_HISTORY_TURNS == 0 or not result.get("sources"):
        return
    with _sessions_lock:
        now = time.time()
        for sid in [k for k, (t, _) in _sessions.items() if now - t > SESSION_TTL_SECONDS]:
            del _sessions[sid]
        entry = _sessions.pop(session_id, None)
        turns = entry[1] if entry else deque(maxlen=CHAT_HISTORY_TURNS)
        turns.append({"question": question, "answer": str(result.get("answer", ""))})
        _sessions[session_id] = (now, turns)  # most recently used goes last
        while len(_sessions) > MAX_SESSIONS:
            _sessions.popitem(last=False)


# ---------------- MCP client ----------------
async def _call_tool(
    name: str,
    args: dict,
) -> Any:
    async with streamable_http_client(MCP_URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            return await session.call_tool(name, args)


async def _list_tools() -> list[Any]:
    async with streamable_http_client(MCP_URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            return [t.name for t in (await session.list_tools()).tools]


class ToolError(RuntimeError):
    """The MCP server was reached, but the ask_faq tool itself failed."""


def _friendly(tool_error: str) -> str:
    t: str = tool_error.lower()
    if "failed to connect" in t or "connection" in t or "timed out" in t:
        return "Could not reach Ollama. Check that it is running and that OLLAMA_URL in src/.env is reachable from the container."
    if "not found" in t and "model" in t:
        return "Ollama does not have the configured model. Run `ollama pull <model>` for OLLAMA_MODEL in src/.env."
    return "The MCP server could not generate an answer. See `docker-compose logs mcp` for details."


def ask_via_mcp(
    question: str,
    top_k: int,
    history: list[dict] | None = None,
) -> dict:
    result: Any = asyncio.run(
        main=_call_tool(
            name="ask_faq",
            args={
                "question": question,
                "top_k": top_k,
                **({"history": history} if history else {}),
            },
        )
    )
    text: LiteralString = "".join(getattr(c, "text", "") for c in result.content)
    if result.isError:
        raise ToolError(text or "ask_faq failed")
    data: Any = result.structuredContent or json.loads(s=text)
    return data.get("result", data) if set(data) == {"result"} else data


# ---------------- Routes ----------------
@app.get("/")
def index() -> Any:
    return send_from_directory(
        app.static_folder,
        "index.html",
    )


@app.get("/docs/<path:filename>")
def docs(filename: str) -> Any:
    """Files from docs/ (the UI shows the architecture diagram from here). send_from_directory refuses
    paths that climb out of the folder."""
    return send_from_directory(DOCS_DIR, filename)


@app.post("/api/ask")
def ask() -> tuple[Any, Literal[400]] | Any | tuple[Any, Literal[502]]:
    data: Any | dict[Any, Any] = request.get_json(silent=True) or {}
    question: str = str(data.get("question") or "").strip()
    if not question:
        return (
            jsonify(
                {
                    "error": "`question` is required",
                }
            ),
            400,
        )
    # The UI's top_k overrides the server default. A missing or non-numeric value falls back to
    # TOP_K_DEFAULT, and the MCP tool does the same for a number outside 1-10.
    try:
        top_k: int = int(data.get("top_k", TOP_K_DEFAULT))
    except (TypeError, ValueError):
        top_k = TOP_K_DEFAULT
    session_id: str | None = _valid_session(data.get("session_id"))
    try:
        result: dict = ask_via_mcp(
            question,
            top_k=top_k,
            history=_get_history(session_id),
        )
        _remember(session_id, question, result)
        return jsonify(result)
    except ToolError as e:
        log.error(msg=f"ask_faq tool failed: {e}")
        return (
            jsonify(
                {
                    "error": _friendly(tool_error=str(e)),
                }
            ),
            502,
        )
    except Exception:
        log.exception(msg="ask via MCP failed")
        return (
            jsonify(
                {
                    "error": "could not get an answer from the MCP server",
                }
            ),
            502,
        )


@app.get("/api/health")
def health() -> Any | tuple[Any, Literal[503]]:
    try:
        return jsonify(
            {
                "status": "ok",
                "mcp_tools": asyncio.run(main=_list_tools()),
            }
        )
    except Exception:
        return (
            jsonify(
                {
                    "status": "mcp server unreachable",
                }
            ),
            503,
        )

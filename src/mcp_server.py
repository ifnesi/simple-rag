from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from typing import Any, Dict, List, Optional

# Settings come from utils/__init__.py (read from the environment and validated there)
from utils import MCP_HOST, MCP_PORT, MCP_TRANSPORT, TOP_K_DEFAULT

# Importing rag_core loads the FAQ files into the in-memory Qdrant (once, at startup)
from utils.rag_core import ask_faq_core

# MCP_TRANSPORT is "stdio" (a client launches this process, as instructions.txt requires) or
# "streamable-http" (long-running server on MCP_PORT, reachable by the web backend and by Claude).

mcp: Any = FastMCP(
    "faq-rag",
    host=MCP_HOST,
    port=MCP_PORT,
    stateless_http=True,  # one tool, no server-initiated messages: no sessions to keep (ignored by stdio)
    # DNS-rebinding protection stays on; list the Host headers we expect.
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=[
            "localhost:*",
            "127.0.0.1:*",
            "mcp:*",
        ],
        allowed_origins=[
            "http://localhost:*",
            "http://127.0.0.1:*",
        ],
    ),
)


@mcp.tool()
def ask_faq(
    question: str,
    top_k: int = TOP_K_DEFAULT,
    history: Optional[List[Dict[str, str]]] = None,
) -> Dict[str, object]:
    """Answer a question from the FAQ corpus. Returns the answer and the source files it came from.
    `history` is optional: earlier {"question", "answer"} pairs of the conversation, oldest first, used
    only to understand follow-up questions."""
    q: str = (question or "").strip()
    if not q:
        raise ValueError("`question` is required")
    return ask_faq_core(
        question=q,
        top_k=top_k if top_k > 0 and top_k <= 10 else TOP_K_DEFAULT,
        history=history,
    )


if __name__ == "__main__":
    mcp.run(transport=MCP_TRANSPORT)

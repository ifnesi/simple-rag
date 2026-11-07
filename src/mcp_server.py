import anyio

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from typing import Any, Dict, List, Optional

# Settings come from utils/__init__.py (read from the environment and validated there)
from utils import MCP_HOST, MCP_PORT, MCP_TRANSPORT, TOP_K_DEFAULT

# Importing rag_core loads the FAQ files into the in-memory Qdrant (once, at startup)
from utils.rag_core import ask_faq_core, list_models as list_models_core

# MCP_TRANSPORT is "stdio" (a client launches this process, as instructions.txt requires) or
# "streamable-http" (long-running server on MCP_PORT, reachable by the web backend and by Claude).

mcp: Any = FastMCP(
    "faq-rag",
    host=MCP_HOST,
    port=MCP_PORT,
    stateless_http=True,  # no server-initiated messages: no sessions to keep (ignored by stdio)
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
async def ask_faq(
    ctx: Context,
    question: str,
    top_k: int = TOP_K_DEFAULT,
    history: Optional[List[Dict[str, str]]] = None,
    model: Optional[str] = None,
) -> Dict[str, object]:
    """Answer a question from the FAQ corpus. Returns the answer and the source files it came from.
    `history` is optional: earlier {"question", "answer"} pairs of the conversation, oldest first, used
    only to understand follow-up questions. `model` is optional: an Ollama model from `list_models`
    (default: the server's OLLAMA_MODEL); an unknown model is an error. While it works, the tool sends standard MCP progress
    notifications (and log messages) describing each step, for clients that ask for them."""
    q: str = (question or "").strip()
    if not q:
        raise ValueError("`question` is required")

    steps = 0

    async def _report(message: str) -> None:
        nonlocal steps
        steps += 1
        try:
            # notifications/progress only goes out if the client sent a progress token
            await ctx.report_progress(progress=steps, total=None, message=message)
            await ctx.info(message)
        except Exception:
            pass  # progress is best effort: it must never fail the answer

    def on_step(message: str) -> None:
        # ask_faq_core is blocking, so it runs in a worker thread; hop back to the event loop to notify
        anyio.from_thread.run(_report, message)

    return await anyio.to_thread.run_sync(
        lambda: ask_faq_core(
            question=q,
            top_k=top_k if top_k > 0 and top_k <= 10 else TOP_K_DEFAULT,
            history=history,
            on_step=on_step,
            model=model,
        )
    )


@mcp.tool()
def list_models() -> Dict[str, object]:
    """List the Ollama models `ask_faq` can use. Returns {"default": "<model>", "models": ["<model>", ...]}."""
    return list_models_core()


if __name__ == "__main__":
    mcp.run(transport=MCP_TRANSPORT)

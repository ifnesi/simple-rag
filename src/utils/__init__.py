"""Settings: every environment variable the code reads, in one place.

Other modules import them from here, e.g. `from utils import OLLAMA_URL`.
This file imports only the standard library, so the web container can use it too.
"""

import os
from pathlib import Path

# ---- FAQ files (existence is checked when they are loaded: the web container has none) ----
FAQ_DIR: Path = Path(
    os.getenv("FAQ_DIR", Path(__file__).parent.parent / "faqs")
)  # src/faqs

# ---- Embeddings and chunking ----
EMBED_MODEL: str = os.getenv("EMBED_MODEL", "BAAI/bge-small-en-v1.5")
CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "1000"))  # max characters per chunk
CHUNK_OVERLAP: int = int(
    os.getenv("CHUNK_OVERLAP", "100")
)  # only used when an entry is split

# ---- Ollama (answer generation) ----
OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2")
OLLAMA_TIMEOUT: float = float(
    os.getenv("OLLAMA_TIMEOUT", "240")
)  # the first call also loads the model
TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0"))

# ---- Retrieval ----
TOP_K_DEFAULT: int = int(os.getenv("TOP_K_DEFAULT", "4"))
# Hits scoring below this cosine similarity are dropped. Tuned for bge-small-en-v1.5, where on-topic
# questions scored 0.68-0.86 and unrelated ones 0.48-0.58: re-measure it if you change EMBED_MODEL.
MIN_SCORE = float(os.getenv("MIN_SCORE", "0.60"))

# ---- MCP server and client ----
MCP_TRANSPORT: str = os.getenv("MCP_TRANSPORT", "stdio")  # "stdio" or "streamable-http"
MCP_HOST: str = os.getenv("MCP_HOST", "127.0.0.1")
MCP_PORT: int = int(os.getenv("MCP_PORT", "8000"))
MCP_URL: str = os.getenv(
    "MCP_URL", "http://mcp:8000/mcp"
)  # where the web backend finds the MCP server

# ---- Validation ----
if not EMBED_MODEL:
    raise ValueError("EMBED_MODEL must not be empty")
if CHUNK_SIZE < 50:
    raise ValueError(f"CHUNK_SIZE must be at least 50, got {CHUNK_SIZE}")
if not 0 <= CHUNK_OVERLAP < CHUNK_SIZE:
    raise ValueError(
        f"CHUNK_OVERLAP must be from 0 to below CHUNK_SIZE ({CHUNK_SIZE}), got {CHUNK_OVERLAP}"
    )
if not OLLAMA_URL.startswith(("http://", "https://")):
    raise ValueError(
        f"OLLAMA_URL must start with http:// or https://, got {OLLAMA_URL!r}"
    )
if not OLLAMA_MODEL:
    raise ValueError("OLLAMA_MODEL must not be empty")
if OLLAMA_TIMEOUT <= 0:
    raise ValueError(f"OLLAMA_TIMEOUT must be above 0, got {OLLAMA_TIMEOUT}")
if not 0 <= TEMPERATURE <= 2:
    raise ValueError(f"TEMPERATURE must be from 0 to 2, got {TEMPERATURE}")
if not 1 <= TOP_K_DEFAULT <= 10:
    raise ValueError(f"TOP_K_DEFAULT must be from 1 to 10, got {TOP_K_DEFAULT}")
if not 0 <= MIN_SCORE <= 1:
    raise ValueError(f"MIN_SCORE must be from 0 to 1, got {MIN_SCORE}")
if MCP_TRANSPORT not in ("stdio", "streamable-http"):
    raise ValueError(
        f'MCP_TRANSPORT must be "stdio" or "streamable-http", got {MCP_TRANSPORT!r}'
    )
if not 1 <= MCP_PORT <= 65535:
    raise ValueError(f"MCP_PORT must be from 1 to 65535, got {MCP_PORT}")
if not MCP_URL.startswith(("http://", "https://")):
    raise ValueError(f"MCP_URL must start with http:// or https://, got {MCP_URL!r}")

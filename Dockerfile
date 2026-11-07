FROM python:3.12-slim

ARG EMBED_MODEL=BAAI/bge-small-en-v1.5
ENV PYTHONUNBUFFERED=1 \
    EMBED_MODEL=${EMBED_MODEL} \
    FASTEMBED_CACHE_PATH=/opt/models

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bake the embedding model into the image so the container needs no internet to embed
RUN python -c "import os; from fastembed import TextEmbedding; TextEmbedding(os.environ['EMBED_MODEL'])"

# Code only: faqs/ is mounted at runtime, .env is never copied (see .dockerignore)
COPY src/ .
# The web UI shows docs/system_architecture_diagram.png in a popup (served by app.py at /docs/...)
COPY docs/ ./docs/

EXPOSE 5000

# Default command = the web backend (the compose `mcp` service overrides it with mcp_server.py)
CMD ["gunicorn", "-w", "1", "--threads", "4", "--timeout", "300", "-b", "0.0.0.0:5000", "app:app"]

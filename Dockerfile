# PPT Master Service
# Python 3.11 slim + git + system deps for lxml / cairosvg / pandoc
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# System deps: git for repo clone, build-essential + libxml2/libxslt for lxml,
# libcairo2 + libpango for cairosvg, pandoc for legacy doc formats.
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        libxml2-dev \
        libxslt1-dev \
        libcairo2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        pandoc \
        curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install our requirements first (better layer caching)
COPY requirements.txt .
RUN pip install --no-input -r requirements.txt

# Copy app code
COPY app/ ./app/
COPY .env.example ./.env.example

# Pre-create data + repo mount points
RUN mkdir -p /data /opt/ppt-master

# Default env (operator overrides via docker-compose env_file)
ENV STORAGE_LOCAL_ROOT=/data \
    PPTMASTER_REPO_DIR=/opt/ppt-master \
    PPTMASTER_AUTO_SETUP=true

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
    CMD curl -fsS http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

# PPT Master Service

A self-hostable backend service that drives [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) via a **mini LLM agent loop** — no Claude Code / Cursor / Codex IDE required. You talk to it over HTTP; it runs the agent for you and streams progress back.


## What it does

- Accepts a job request: prompt + uploaded source files (PDF/DOCX/etc.).
- Spawns a mini agent loop that:
  1. Loads the PPT Master `SKILL.md` as its system prompt.
  2. Calls tools (read file, write SVG, run `image_search.py`, finalize deck, ...) to drive the pipeline.
  3. Streams every thought, tool call, and tool result as events.
- Stages the produced `.pptx` to `exports/` and exposes a download URL.
- Persists job state, supports cancellation, and dispatches webhook events.

You keep control of which LLM is the brain (OpenAI / Anthropic / Gemini / Kimi), where files live (local disk or S3), and how the client observes progress (REST polling, WebSocket, or webhook — or all three).

## Architecture

```
                     ┌─────────────────────────────────────────┐
   Client  ────────► │ FastAPI (REST + WS + SSE)               │
   (HTTP)            │  - X-API-Key auth                       │
                     │  - POST /jobs  (multipart upload)       │
                     │  - GET  /jobs/{id}  (status + history)  │
                     │  - WS   /jobs/{id}/stream               │
                     │  - GET  /jobs/{id}/events  (SSE)        │
                     │  - POST /jobs/{id}/cancel               │
                     │  - GET  /jobs/{id}/download             │
                     └────────────┬────────────────────────────┘
                                  │
                     ┌────────────▼────────────┐
                     │ JobManager              │  asyncio.Semaphore
                     │  QUEUED→RUNNING→DONE    │  bounds concurrency
                     │  persists jobs.json     │
                     └────────────┬────────────┘
                                  │ per-job Task
                     ┌────────────▼────────────┐
                     │ AgentLoop               │
                     │  - system = SKILL.md    │
                     │  - tool-calling loop    │
                     │  - iteration cap        │
                     └──┬─────────┬────────────┘
                        │         │
              ┌─────────▼─┐   ┌───▼───────────────┐
              │ LLM       │   │ ToolRegistry      │
              │ abstract  │   │  read_skill_md    │
              │ (4 impls) │   │  read/write_file  │
              └───────────┘   │  run_pptmaster_*  │
                              │  http_get         │
                              │  finalize_deck    │
                              │  progress         │
                              └───────┬───────────┘
                                      │ subprocess
                              ┌───────▼───────────┐
                              │ PPT Master repo   │  (auto-cloned)
                              │  projects/<id>/   │
                              │  exports/*.pptx   │
                              └───────────────────┘
                                      │
                              ┌───────▼───────────┐
                              │ StorageBackend    │  local | S3
                              └───────────────────┘
```

A single `EventBus` fans every event to three sinks simultaneously:
- the **persisted event log** (REST `GET /jobs/{id}` reads it),
- any **WebSocket subscriber** (`/jobs/{id}/stream`),
- the optional **webhook dispatcher** (POSTs to your URL, HMAC-signed).

## Quick start (Docker Compose)

```bash
git clone <this-repo> ppt-master-service
cd ppt-master-service
cp .env.example .env
# Edit .env:
#   - set API_KEYS to a strong random string
#   - set LLM_PROVIDER and the matching API key
#   - leave PPTMASTER_AUTO_SETUP=true so the container clones the repo
docker compose up -d
curl http://localhost:8000/health
```

First boot will clone the PPT Master repo and `pip install` its requirements (takes ~2 min). Health check `start_period` is 120s to accommodate this.

## Quick start (without Docker)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env as above
# Pre-clone the repo so the runtime finds SKILL.md:
git clone --depth 1 https://github.com/hugohe3/ppt-master.git /opt/ppt-master
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Configuration

All settings live in `.env` (see `.env.example`). The most important:

| Var | Purpose |
|---|---|
| `API_KEYS` | Comma-separated valid client keys (sent as `X-API-Key`). |
| `LLM_PROVIDER` | `openai` \| `anthropic` \| `gemini` \| `kimi` \| `azure` \| `custom`. |
| `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` / `GEMINI_API_KEY` / `KIMI_API_KEY` | The corresponding SDK key. |
| `CUSTOM_BASE_URL` / `LLM_MODEL_CUSTOM` / `CUSTOM_API_KEY` | Enable the **custom** provider for any OpenAI-compatible endpoint (key optional for local servers). `CUSTOM_LABEL` renames it in the UI. |
| `LLM_MAX_ITERATIONS` | Hard cap on agent turns (default 40). Bounding cost. |
| `MAX_CONCURRENT_JOBS` | In-process semaphore bound (default 2). |
| `MAX_JOB_TIMEOUT_SECONDS` | Per-job wall-clock cap (default 1800). |
| `STORAGE_BACKEND` | `local` \| `s3`. |
| `STORAGE_LOCAL_ROOT` | Where uploads/exports live (default `/data`). |
| `STORAGE_S3_BUCKET` / `STORAGE_S3_PREFIX` / `STORAGE_S3_REGION` | S3 backend config. |
| `PPTMASTER_AUTO_SETUP` | Clone repo + install its deps on boot. |
| `PPTMASTER_REPO_DIR` | Where the upstream repo lives (default `/opt/ppt-master`). |
| `ALLOWED_ROUTES` | Subset of `create,edit,template,postprocess` this instance accepts. |
| `WEBHOOK_DEFAULT_URL` / `WEBHOOK_SECRET` | Default webhook target + HMAC secret. |

## API

All endpoints except `/health` require `X-API-Key: <key>` (WebSocket uses `?api_key=<key>` query param).

### Create a job (file upload)

```bash
curl -X POST http://localhost:8000/jobs \
  -H "X-API-Key: $KEY" \
  -F "prompt=Create a 10-slide PPT from this report" \
  -F "route=create" \
  -F "files=@/path/to/report.pdf"
```

Response:
```json
{ "job_id": "a1b2c3...", "status": "queued", "sources": ["a1b2c3.../sources/report.pdf"] }
```

### Create a job (JSON, sources already in storage)

```bash
curl -X POST http://localhost:8000/jobs/json \
  -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
  -d '{"prompt":"Create a PPT from sources/x.pdf","route":"create","sources":["abc/sources/x.pdf"]}'
```

### Poll status

```bash
curl http://localhost:8000/jobs/$JOB_ID -H "X-API-Key: $KEY"
```

Includes `status`, `usage`, `export_path`, and full `events` history.

### Stream live events (WebSocket)

```javascript
const ws = new WebSocket(`ws://localhost:8000/jobs/${jobId}/stream?api_key=${KEY}`);
ws.onmessage = (e) => console.log(JSON.parse(e.data));
// Each frame: { job_id, type, timestamp, data }
// Terminal types: job.completed | job.failed | job.cancelled
```

### Stream live events (SSE — REST-friendly)

```bash
curl -N http://localhost:8000/jobs/$JOB_ID/events -H "X-API-Key: $KEY"
```

### Webhook

Pass `webhook_url` (and optionally `webhook_secret`) when creating a job. The service POSTs each event to your URL with `X-PPTMaster-Signature: sha256=<hmac>` header. Body is the event JSON. Retry: 3 attempts with exponential backoff. Terminal events end the dispatch loop.

### Download the deck

```bash
curl -o deck.pptx http://localhost:8000/jobs/$JOB_ID/download -H "X-API-Key: $KEY"
```

### Cancel

```bash
curl -X POST http://localhost:8000/jobs/$JOB_ID/cancel -H "X-API-Key: $KEY"
```

Sets a stop flag the agent loop checks between iterations (cancellation is cooperative, not preemptive).

## How the agent drives PPT Master

The agent loop exposes these tools to the LLM:

| Tool | Purpose |
|---|---|
| `read_skill_md` | Load `SKILL.md` workflow rules into context. |
| `list_project_files` | List user-uploaded sources. |
| `read_file` | Read text/PDF/DOCX from the workdir (returns extracted text). |
| `write_file` | Write SVG / notes / manifest into the workdir. |
| `list_dir` | Inspect the workdir. |
| `run_pptmaster_script` | Run `image_gen.py` / `image_search.py` / `update_repo.py` in a subprocess. |
| `http_get` | Fetch an image URL (≤10MB) into the workdir. |
| `progress` | Emit a client-visible progress message (stage, percent, message). |
| `finalize_deck` | Stage the produced `.pptx` to `exports/` and end the job. |

Each job gets a private sandbox at `<repo>/projects/<job_id>/` with a `sources/` subdir. The LLM cannot escape this sandbox (path traversal is rejected).

The system prompt is `SKILL.md + a short operating preamble` that constrains the model to: call `read_skill_md` first, use tools (never direct file writes), emit progress regularly, and call `finalize_deck` when done.

## LLM provider notes

- **Anthropic Claude** (recommended): native content-block tool calling, matches PPT Master's intended design.
- **OpenAI / Kimi**: OpenAI-compatible; Kimi uses `https://api.moonshot.cn/v1` and a 128K–1M context model.
- **Gemini**: 1M+ context, ideal for long source documents.
- **Custom (OpenAI-compatible)**: point `CUSTOM_BASE_URL` + `LLM_MODEL_CUSTOM` at any endpoint speaking the OpenAI Chat Completions API (Groq, OpenRouter, Together, vLLM, Ollama, LM Studio, DeepSeek, your own gateway). Set `CUSTOM_API_KEY` if the endpoint needs auth; `CUSTOM_LABEL` renames it in the web UI.
- Switch at runtime via `LLM_PROVIDER` env var, or per-job via `provider_override` in the JSON request body.

The provider abstraction (`app/llm/base.py`) normalizes every provider's response into the same shape (`LLMContent[]` with `text` and `tool_use` blocks), so the agent loop is provider-agnostic.

## Storage backends

- **local** (default): files under `STORAGE_LOCAL_ROOT`. The agent's workdir lives under the PPT Master repo's `projects/` tree; uploads are copied into it.
- **s3**: source files and exports live in S3; `make_local_path` downloads to a temp cache so the PPT Master subprocess still gets a real path. Pre-signed URLs available via `public_url()`.

Adding a new backend = implement `StorageBackend` and add a branch in `app/storage/factory.py`.

## Scaling

This is a single-worker, single-process design (the in-process `EventBus` and `asyncio.Semaphore` don't cross process boundaries). For higher throughput:

1. Run N replicas behind a load balancer.
2. Switch `STORAGE_BACKEND=s3`.
3. Replace `EventBus` with Redis pub/sub (the interface is already narrow — `subscribe` / `publish` / `get_log`).
4. Replace the in-process `asyncio.Semaphore` with a Redis-based distributed lock.

The agent loop, tool registry, LLM abstraction, and storage abstraction are all unchanged by that migration.

## Limitations & honest notes

- **Quality is the model's ceiling.** PPT Master only owns the workflow; the LLM does the analysis and per-page design. A weak model produces a weak deck — that's not a service bug. (See the upstream `harness + model = agent` framing.)
- **Cost is real.** Page-by-page design + tool calling is token-heavy. `LLM_MAX_ITERATIONS` and `MAX_JOB_TIMEOUT_SECONDS` bound it but don't make it cheap.
- **The pipeline does not (yet) include a built-in DrawingML/SVG→PPTX exporter.** The `finalize_deck` tool stages whatever `.pptx` the agent produces (via `python-pptx` in its tool calls). If you want full parity with the upstream SVG-rendering pipeline, that logic would live in a new tool — the architecture supports adding it without touching the loop.
- **Cancellation is cooperative.** The loop checks the stop flag between iterations, not mid-tool-call.
- **No multi-tenant isolation beyond API key.** All valid keys see all jobs. Add per-key scoping in `JobManager` if you need it.

## Verification

Smoke tests (no LLM calls, no API keys needed):

```bash
python tests/test_smoke.py
```

Checks: imports clean, `/health` responds, API key auth enforced, route validation works.

## Project layout

```
app/
  config.py            # pydantic-settings
  events.py            # EventBus + Event types (REST/WS/webhook share this)
  webhooks.py          # HMAC-signed webhook dispatcher with retries
  storage/             # base + local + s3 + factory
  llm/                 # base + openai(+kimi) + anthropic + gemini + factory
  agent/
    tools.py           # tool registry + 9 concrete tools
    loop.py            # orchestration loop with iteration cap
  jobs/
    manager.py         # asyncio job state machine + persistence
  pptmaster/
    runtime.py         # auto-clone + deps + path helpers
  api/
    auth.py            # X-API-Key header + WS query param
    routes.py          # REST + WS + SSE
  main.py              # FastAPI app + lifespan
tests/test_smoke.py
Dockerfile
docker-compose.yml
requirements.txt
.env.example
```

## License

This service wrapper is your own (do what you want with it). The upstream [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) retains its own license — check the repo.

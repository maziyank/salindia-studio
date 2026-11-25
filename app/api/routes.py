"""HTTP + WebSocket routes.

Endpoints:
  GET  /health                  -> service health (no auth)
  POST /jobs                    -> create job (multipart: files + JSON spec)
  GET  /jobs                    -> list jobs
  GET  /jobs/{id}               -> job status + history
  POST /jobs/{id}/cancel        -> request cancellation
  GET  /jobs/{id}/events        -> SSE stream of events (REST-friendly)
  WS   /jobs/{id}/stream        -> live event stream (JSON frames)
  GET  /jobs/{id}/download      -> download the produced .pptx
  GET  /files/{path:path}       -> read a stored file (for S3 backend fallback)
  GET  /jobs/{id}/export        -> download the staged .pptx from exports/ (no auth, browser-friendly)
  GET  /                        -> built-in web UI
"""
from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    Request,
    UploadFile,
    WebSocket,
    WebSocketDisconnect,
    status,
)
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from app.api.auth import require_api_key, require_api_key_sse, require_api_key_ws
from app.config import get_settings
from app.events import EventBus, EventType, bus
from app.jobs.manager import JobManager, JobSpec, get_job_manager
from app.llm.factory import list_available_providers
from app.pptmaster.runtime import get_runtime
from app.storage.factory import get_storage

router = APIRouter()

_WEB_INDEX = Path(__file__).resolve().parents[2] / "web" / "index.html"


# ---------------------------------------------------------------------------
# Web UI
# ---------------------------------------------------------------------------

@router.get("/", include_in_schema=False)
async def ui_index() -> HTMLResponse:
    """Serve the single-file web UI."""
    if not _WEB_INDEX.exists():
        raise HTTPException(404, "UI not found")
    return HTMLResponse(_WEB_INDEX.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------

@router.get("/health", tags=["meta"])
async def health() -> dict:
    s = get_settings()
    rt = get_runtime()
    return {
        "status": "ok" if rt.is_ready else "degraded",
        "ppt_master_ready": rt.is_ready,
        "ppt_master_error": rt.last_error,
        "storage_backend": s.storage_backend,
        "llm_provider": s.llm_provider,
        "available_providers": list_available_providers(),
        "allowed_routes": s.allowed_routes,
        "max_concurrent_jobs": s.max_concurrent_jobs,
    }


# ---------------------------------------------------------------------------
# Job creation
# ---------------------------------------------------------------------------

class JobCreateRequest(BaseModel):
    """JSON-body variant of POST /jobs (used when no file upload)."""
    prompt: str = Field(..., description="Instruction for the agent, e.g. 'Create a PPT from sources/report.pdf'")
    route: str = "create"
    sources: List[str] = Field(default_factory=list, description="Logical paths to files already in storage")
    provider_override: Optional[str] = None
    webhook_url: Optional[str] = None
    webhook_secret: Optional[str] = None
    no_confirm: bool = True
    options: dict = Field(default_factory=dict)


async def _save_uploads(job_id_prefix: str, files: List[UploadFile]) -> List[str]:
    """Save uploaded files into storage under <job_id_prefix>/sources/ and
    return their logical paths.
    """
    storage = get_storage()
    out: List[str] = []
    for f in files:
        if not f.filename:
            continue
        logical = f"{job_id_prefix}/sources/{f.filename}"
        data = await f.read()
        await storage.put(logical, data, content_type=f.content_type or "application/octet-stream")
        out.append(logical)
    return out


@router.post("/jobs", tags=["jobs"], dependencies=[Depends(require_api_key)])
async def create_job(
    request: Request,
    prompt: str = Form(...),
    route: str = Form("create"),
    provider_override: Optional[str] = Form(None),
    webhook_url: Optional[str] = Form(None),
    webhook_secret: Optional[str] = Form(None),
    no_confirm: bool = Form(True),
    options: Optional[str] = Form(None),
    files: List[UploadFile] = File(default=[]),
) -> dict:
    """Create a job. Use multipart/form-data when uploading files; the prompt
    is a form field. Uploaded files are stored at `<random>/sources/<name>`
    and their logical paths are passed to the agent as the source list.
    `options` may carry a JSON object of structured job options (e.g. a design spec).
    """
    mgr = get_job_manager()
    parsed_options: dict = {}
    if options:
        try:
            parsed_options = json.loads(options)
        except json.JSONDecodeError:
            raise HTTPException(400, "options must be a JSON object")
    # Pre-generate job_id so we can stash uploads under it
    import uuid
    job_id = uuid.uuid4().hex
    sources = await _save_uploads(job_id, files)
    # Compose prompt: append source list so the agent knows what to read
    full_prompt = prompt
    if sources:
        names = ", ".join(Path(s).name for s in sources)
        full_prompt = f"{prompt}\n\nSource files (under projects/{job_id}/sources/): {names}"
    spec = JobSpec(
        prompt=full_prompt,
        route=route,
        sources=sources,
        provider_override=provider_override,
        webhook_url=webhook_url,
        webhook_secret=webhook_secret,
        no_confirm=no_confirm,
        options=parsed_options if isinstance(parsed_options, dict) else {},
    )
    # The manager will mint its own job_id; to keep uploads aligned we pass
    # the pre-staged paths and let the manager stage them into the workdir.
    # To avoid id mismatch, override the manager's id by re-staging: simplest
    # is to call a variant. We'll just create with our id:
    rec = await _create_with_id(mgr, job_id, spec)
    return {"job_id": rec.job_id, "status": rec.status, "sources": sources}


async def _create_with_id(mgr: JobManager, job_id: str, spec: JobSpec):
    """Bypass the manager's UUID generation so uploads land in the same
    namespace as the agent's workdir."""
    import time
    from app.jobs.manager import JobRecord
    from app.events import Event, EventType, bus
    rec = JobRecord(
        job_id=job_id,
        status="queued",
        spec=spec.__dict__,
        created_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        source_files=list(spec.sources),
    )
    mgr._records[job_id] = rec
    await mgr._persist()
    await bus.publish(Event(job_id=job_id, type=EventType.JOB_CREATED, data={"spec": spec.__dict__}))
    wh_url = spec.webhook_url or mgr.settings.webhook_default_url
    if wh_url:
        asyncio.create_task(mgr._webhook_dispatcher(job_id, wh_url, spec.webhook_secret or mgr.settings.webhook_secret))
    mgr._tasks[job_id] = asyncio.create_task(mgr._run_job(job_id, spec))
    return rec


@router.post("/jobs/json", tags=["jobs"], dependencies=[Depends(require_api_key)])
async def create_job_json(req: JobCreateRequest) -> dict:
    """JSON-only job creation (no file upload). Use this when sources are
    already in storage and you have their logical paths."""
    mgr = get_job_manager()
    rec = await mgr.create_job(JobSpec(
        prompt=req.prompt, route=req.route, sources=req.sources,
        provider_override=req.provider_override, webhook_url=req.webhook_url,
        webhook_secret=req.webhook_secret, no_confirm=req.no_confirm, options=req.options,
    ))
    return {"job_id": rec.job_id, "status": rec.status, "sources": rec.source_files}


# ---------------------------------------------------------------------------
# Job status / list / cancel
# ---------------------------------------------------------------------------

@router.get("/jobs", tags=["jobs"], dependencies=[Depends(require_api_key)])
async def list_jobs(limit: int = 100) -> dict:
    mgr = get_job_manager()
    return {"jobs": [r.to_dict() for r in mgr.list_jobs(limit=limit)]}


@router.get("/jobs/{job_id}", tags=["jobs"], dependencies=[Depends(require_api_key)])
async def get_job(job_id: str) -> dict:
    mgr = get_job_manager()
    rec = mgr.get(job_id)
    if not rec:
        raise HTTPException(404, "job not found")
    events = [e.to_dict() for e in bus.get_log(job_id)]
    return {**rec.to_dict(), "events": events}


@router.post("/jobs/{job_id}/cancel", tags=["jobs"], dependencies=[Depends(require_api_key)])
async def cancel_job(job_id: str) -> dict:
    mgr = get_job_manager()
    ok = await mgr.cancel(job_id)
    return {"cancelled": ok}


# ---------------------------------------------------------------------------
# Live event streams
# ---------------------------------------------------------------------------

@router.get("/jobs/{job_id}/events", tags=["jobs"], dependencies=[Depends(require_api_key_sse)])
async def job_events_sse(job_id: str, request: Request) -> StreamingResponse:
    """Server-Sent Events stream of job events. Replays history on connect."""
    mgr = get_job_manager()
    if not mgr.get(job_id):
        raise HTTPException(404, "job not found")

    async def gen():
        q = await bus.subscribe(job_id)
        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    ev = await asyncio.wait_for(q.get(), timeout=15.0)
                    yield f"data: {json.dumps(ev.to_dict())}\n\n"
                except asyncio.TimeoutError:
                    yield ": keepalive\n\n"
        finally:
            await bus.unsubscribe(job_id, q)

    return StreamingResponse(gen(), media_type="text/event-stream")


@router.websocket("/jobs/{job_id}/stream")
async def job_events_ws(websocket: WebSocket, job_id: str) -> None:
    """WebSocket stream. Authenticate via ?api_key=... query param."""
    try:
        await require_api_key_ws(websocket.query_params.get("api_key"))
    except HTTPException:
        await websocket.close(code=4401)
        return
    mgr = get_job_manager()
    if not mgr.get(job_id):
        await websocket.close(code=4404)
        return
    await websocket.accept()
    q = await bus.subscribe(job_id)
    try:
        while True:
            try:
                ev = await asyncio.wait_for(q.get(), timeout=30.0)
                await websocket.send_json(ev.to_dict())
                if ev.type in (EventType.JOB_COMPLETED, EventType.JOB_FAILED, EventType.JOB_CANCELLED):
                    await asyncio.sleep(0.5)
                    await websocket.close()
                    return
            except asyncio.TimeoutError:
                # keepalive ping
                await websocket.send_json({"type": "ping"})
    except WebSocketDisconnect:
        pass
    finally:
        await bus.unsubscribe(job_id, q)


# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------

@router.get("/jobs/{job_id}/download", tags=["jobs"], dependencies=[Depends(require_api_key)])
async def download_job(job_id: str) -> StreamingResponse:
    mgr = get_job_manager()
    rec = mgr.get(job_id)
    if not rec:
        raise HTTPException(404, "job not found")
    if not rec.export_path or not Path(rec.export_path).exists():
        raise HTTPException(404, "export not ready")
    return FileResponse(rec.export_path, media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        filename=rec.export_name or f"{job_id}.pptx")


@router.get("/jobs/{job_id}/export", tags=["jobs"])
async def download_export(job_id: str) -> FileResponse:
    """Download the produced .pptx straight from exports/ without an API key.

    Used by the built-in browser UI (which cannot set the X-API-Key header on
    a plain download link). Serves only *.pptx files under the exports dir.
    """
    rt = get_runtime()
    exports = rt.exports_dir.resolve()
    target: Optional[Path] = None
    for p in sorted(exports.glob(f"{job_id}*.pptx"), key=lambda x: x.stat().st_mtime, reverse=True):
        if p.is_file() and p.resolve().parent == exports:
            target = p
            break
    if not target:
        raise HTTPException(404, "export not ready")
    return FileResponse(target, media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        filename=target.name)


# ---------------------------------------------------------------------------
# Raw file access (for S3 backend where local paths don't exist)
# ---------------------------------------------------------------------------

@router.get("/files/{path:path}", tags=["files"], dependencies=[Depends(require_api_key)])
async def get_file(path: str) -> StreamingResponse:
    storage = get_storage()
    if not await storage.exists(path):
        raise HTTPException(404, "not found")
    data = await storage.get(path)
    return StreamingResponse(iter([data]))

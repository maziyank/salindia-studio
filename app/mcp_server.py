"""MCP server: exposes this service to MCP clients (Claude Code, Cursor, ...).

Transport: streamable HTTP, mounted by `app.main` at `MCP_PATH` (default
`/mcp`). Every request must carry the same `X-API-Key` (or
`Authorization: Bearer`) the REST API accepts — see `MCPAuthMiddleware`.

Tools mirror the REST endpoints:
  create_deck_job  -> POST /jobs (with optional base64 file uploads)
  get_job          -> GET  /jobs/{id}
  list_jobs        -> GET  /jobs
  cancel_job       -> POST /jobs/{id}/cancel
Resource:
  salindia://jobs/{job_id}/deck -> the produced .pptx as a binary blob
"""
from __future__ import annotations

import base64
import binascii
import mimetypes
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.exceptions import ToolError
from mcp.server.transport_security import TransportSecuritySettings
from mcp.types import ToolAnnotations

from app.config import get_settings
from app.events import bus
from app.jobs.manager import JobSpec, get_job_manager
from app.storage.factory import get_storage

PPTX_MIME = "application/vnd.openxmlformats-officedocument.presentationml.presentation"

_settings = get_settings()

# The SDK rejects requests whose Host header isn't in an allowlist (anti
# DNS-rebinding), which breaks any deployment behind a real hostname. Enable
# it only when MCP_ALLOWED_HOSTS lists the hosts this service is served under.
_transport_security = (
    TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=_settings.mcp_allowed_hosts,
    )
    if _settings.mcp_allowed_hosts
    else TransportSecuritySettings(enable_dns_rebinding_protection=False)
)

mcp = FastMCP(
    "salindia-studio",
    instructions=(
        "Salindia Studio turns a prompt (+ optional source documents) into a "
        ".pptx deck. Call create_deck_job, then poll get_job until status is "
        "'completed' (or 'failed'/'cancelled'), then read the resource "
        "salindia://jobs/{job_id}/deck to download the deck."
    ),
    # Mounted at "/" by app.main, so this is the full endpoint path.
    streamable_http_path=_settings.mcp_path,
    stateless_http=True,
    json_response=True,
    transport_security=_transport_security,
)

_http_app = None


def get_mcp_http_app():
    """Build (once per lifespan) the streamable-HTTP ASGI app.

    Must be called before `mcp.session_manager` is usable: the session manager
    is created lazily inside `streamable_http_app()`, and the host app's
    lifespan has to run it (a mounted app's own lifespan never runs).
    """
    global _http_app
    if _http_app is None:
        _http_app = mcp.streamable_http_app()
    return _http_app


def reset_mcp_http_app() -> None:
    """Discard the cached ASGI app and session manager.

    `StreamableHTTPSessionManager.run()` may only be entered once per instance,
    so any process that starts the host lifespan more than once (tests, embedded
    use) needs a fresh manager each time. FastMCP exposes no public reset, hence
    the private attribute.
    """
    global _http_app
    _http_app = None
    mcp._session_manager = None


class MCPMount:
    """ASGI passthrough mounted by `app.main` at "/".

    Resolving the MCP app per request lets `reset_mcp_http_app()` swap in a new
    streamable-HTTP app between lifespans without rebuilding the FastAPI app.
    """

    async def __call__(self, scope, receive, send) -> None:
        await get_mcp_http_app()(scope, receive, send)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _record_or_error(job_id: str):
    rec = get_job_manager().get(job_id)
    if not rec:
        raise ToolError(f"job not found: {job_id}")
    return rec


async def _save_uploads(job_id: str, files: List[Dict[str, str]]) -> List[str]:
    """Store base64-encoded files under `<job_id>/sources/` and return their
    logical storage paths."""
    storage = get_storage()
    limit = get_settings().max_source_size_mb * 1024 * 1024
    out: List[str] = []
    for f in files:
        name = Path(str(f.get("filename", ""))).name
        if not name:
            raise ToolError("each file needs a 'filename'")
        try:
            data = base64.b64decode(f.get("content_base64") or "", validate=True)
        except (binascii.Error, ValueError) as e:
            raise ToolError(f"file {name!r}: content_base64 is not valid base64 ({e})")
        if len(data) > limit:
            raise ToolError(f"file {name!r} exceeds MAX_SOURCE_SIZE_MB ({get_settings().max_source_size_mb})")
        logical = f"{job_id}/sources/{name}"
        content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
        await storage.put(logical, data, content_type=content_type)
        out.append(logical)
    return out


def _find_export(job_id: str) -> Optional[Path]:
    """Locate the staged .pptx for a job (same lookup as GET /jobs/{id}/export)."""
    from app.pptmaster.runtime import get_runtime

    exports = get_runtime().exports_dir.resolve()
    for p in sorted(exports.glob(f"{job_id}*.pptx"), key=lambda x: x.stat().st_mtime, reverse=True):
        if p.is_file() and p.resolve().parent == exports:
            return p
    return None


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

@mcp.tool(
    title="Create deck job",
    annotations=ToolAnnotations(title="Create deck job", readOnlyHint=False, destructiveHint=False),
)
async def create_deck_job(
    prompt: str,
    route: str = "create",
    sources: Optional[List[str]] = None,
    files: Optional[List[Dict[str, str]]] = None,
    provider_override: Optional[str] = None,
    webhook_url: Optional[str] = None,
    options: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Start a deck-generation job. Returns immediately with a job_id; poll
    `get_job` for progress.

    Args:
        prompt: What to build, e.g. "Create a 10-slide deck from the report".
        route: PPT Master route (create | edit | template | postprocess).
        sources: Logical paths of files already in storage (see /jobs/json).
        files: Files to upload inline, each {"filename": str, "content_base64": str}.
        provider_override: LLM provider for this job (openai | anthropic | gemini | kimi | azure | custom).
        webhook_url: Optional URL to receive HMAC-signed job events.
        options: Structured job options, e.g. {"design_spec": "..."}.
    """
    mgr = get_job_manager()
    if route.lower() not in mgr.settings.allowed_routes:
        raise ToolError(f"route {route!r} not allowed (allowed: {mgr.settings.allowed_routes})")

    job_id = uuid.uuid4().hex
    stored = await _save_uploads(job_id, files or [])
    all_sources = list(sources or []) + stored

    full_prompt = prompt
    if all_sources:
        names = ", ".join(Path(s).name for s in all_sources)
        full_prompt = f"{prompt}\n\nSource files (under projects/{job_id}/sources/): {names}"

    rec = await mgr.create_job_with_id(job_id, JobSpec(
        prompt=full_prompt,
        route=route,
        sources=all_sources,
        provider_override=provider_override,
        webhook_url=webhook_url,
        options=options or {},
    ))
    return {"job_id": rec.job_id, "status": rec.status, "sources": all_sources}


@mcp.tool(
    title="Get job",
    annotations=ToolAnnotations(title="Get job", readOnlyHint=True),
)
def get_job(job_id: str, include_events: bool = False, event_limit: int = 50) -> Dict[str, Any]:
    """Status of a job, including usage and (optionally) the tail of its event log."""
    rec = _record_or_error(job_id)
    out = rec.to_dict()
    if include_events:
        out["events"] = [e.to_dict() for e in bus.get_log(job_id)][-max(1, event_limit):]
    return out


@mcp.tool(
    title="List jobs",
    annotations=ToolAnnotations(title="List jobs", readOnlyHint=True),
)
def list_jobs(limit: int = 20) -> Dict[str, Any]:
    """Most recent jobs, newest last."""
    return {"jobs": [r.to_dict() for r in get_job_manager().list_jobs(limit=max(1, limit))]}


@mcp.tool(
    title="Cancel job",
    annotations=ToolAnnotations(title="Cancel job", readOnlyHint=False, destructiveHint=True, idempotentHint=True),
)
async def cancel_job(job_id: str) -> Dict[str, Any]:
    """Request cancellation. Cooperative: the agent stops between iterations."""
    _record_or_error(job_id)
    return {"cancelled": await get_job_manager().cancel(job_id)}


# ---------------------------------------------------------------------------
# Resource: the produced deck
# ---------------------------------------------------------------------------

@mcp.resource(
    "salindia://jobs/{job_id}/deck",
    name="deck",
    description="The generated .pptx for a completed job.",
    mime_type=PPTX_MIME,
)
def job_deck(job_id: str) -> bytes:
    rec = _record_or_error(job_id)
    if rec.status != "completed":
        raise ToolError(f"job {job_id} is {rec.status}; deck is not ready")
    path = _find_export(job_id)
    if not path:
        raise ToolError(f"export file not found for job {job_id}")
    return path.read_bytes()

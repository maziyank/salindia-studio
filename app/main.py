"""FastAPI app entrypoint.

Lifespan:
  - On startup: provision the PPT Master repo (async, runs in thread),
    load persisted job records, run the MCP session manager, configure logging.
  - On shutdown: cancel running jobs gracefully.

Run with:  uvicorn app.main:app --host 0.0.0.0 --port 8000
"""
from __future__ import annotations

import asyncio
import logging
from contextlib import AsyncExitStack, asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.api.auth import MCPAuthMiddleware
from app.api.routes import router
from app.config import get_settings
from app.jobs.manager import get_job_manager
from app.mcp_server import MCPMount, get_mcp_http_app, mcp, reset_mcp_http_app
from app.pptmaster.runtime import get_runtime


@asynccontextmanager
async def lifespan(app: FastAPI):
    s = get_settings()
    logging.basicConfig(
        level=getattr(logging, s.app_log_level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    log = logging.getLogger("startup")
    log.info("provisioning PPT Master runtime (auto_setup=%s)...", s.pptmaster_auto_setup)
    rt = get_runtime()
    await rt.setup_async()
    if rt.is_ready:
        log.info("PPT Master ready at %s", rt.repo_dir)
    else:
        log.warning("PPT Master NOT ready: %s", rt.last_error)

    mgr = get_job_manager()
    await mgr.load_persisted()

    async with AsyncExitStack() as stack:
        if s.mcp_enabled:
            # A mounted app's own lifespan never runs, so drive the MCP
            # session manager from here. Rebuild it each lifespan: the manager
            # can only be run once per instance.
            reset_mcp_http_app()
            get_mcp_http_app()  # creates the session manager lazily
            await stack.enter_async_context(mcp.session_manager.run())
            log.info("MCP server enabled at %s", s.mcp_path)
        yield

    # Shutdown: cancel running tasks
    log.info("shutdown: cancelling %d running jobs", len(mgr._tasks))
    for jid, task in list(mgr._tasks.items()):
        task.cancel()


def create_app() -> FastAPI:
    s = get_settings()
    app = FastAPI(
        title="Salindia Studio",
        description="Backend service that drives hugohe3/ppt-master via a mini LLM agent loop.",
        version="0.1.0",
        lifespan=lifespan,
    )
    if s.mcp_enabled:
        # Added before CORS so CORS stays the outermost middleware (its headers
        # then also apply to 401s from MCPAuthMiddleware).
        app.add_middleware(MCPAuthMiddleware, path_prefix=s.mcp_path, api_keys=s.api_keys)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Convert ValueError (e.g. disallowed route) to a clean 400 instead of 500.
    @app.exception_handler(ValueError)
    async def _value_error_handler(request: Request, exc: ValueError):
        return JSONResponse(status_code=400, content={"error": "bad_request", "detail": str(exc)})

    app.include_router(router)
    # Static UI assets (favicon, Open Graph image, web manifest).
    web_dir = Path(__file__).resolve().parents[1] / "web"
    if web_dir.is_dir():
        app.mount("/static", StaticFiles(directory=web_dir), name="static")
    if s.mcp_enabled:
        # Mounted at "/" and last, so the MCP app only sees paths no REST route
        # matched. Mounting at s.mcp_path instead would 307-redirect POST /mcp
        # to /mcp/, which some MCP clients refuse to follow.
        app.mount("/", MCPMount())
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    s = get_settings()
    uvicorn.run("app.main:app", host=s.app_host, port=s.app_port,
                log_level=s.app_log_level, reload=False)

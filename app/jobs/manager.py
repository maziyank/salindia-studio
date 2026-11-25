"""In-process asyncio job manager.

State machine:
  QUEUED -> RUNNING -> (COMPLETED | FAILED | CANCELLED)

A bounded semaphore enforces MAX_CONCURRENT_JOBS. Each job runs in its own
asyncio Task; the agent loop runs inside that task. Job state is persisted
to a JSON file under storage so a server restart can show historical jobs
(restoration of running jobs is NOT supported in this single-process design
- they would be marked FAILED on restart).
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
import uuid
from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.agent.loop import AgentLoop
from app.config import get_settings
from app.events import Event, EventType, JobStatus, bus
from app.storage.factory import get_storage
from app.storage.base import StorageBackend
from app.webhooks import dispatch_event

log = logging.getLogger("jobs.manager")


# ---------------------------------------------------------------------------
# Job spec / record
# ---------------------------------------------------------------------------

@dataclass
class JobSpec:
    """Request payload accepted by POST /jobs."""
    prompt: str
    route: str = "create"            # create | edit | template | postprocess
    sources: List[str] = field(default_factory=list)  # logical paths in storage
    provider_override: Optional[str] = None
    webhook_url: Optional[str] = None
    webhook_secret: Optional[str] = None
    no_confirm: bool = True          # service mode: never asks for confirmation
    options: Dict[str, Any] = field(default_factory=dict)


@dataclass
class JobRecord:
    job_id: str
    status: str               # JobStatus value
    spec: Dict[str, Any]
    created_at: str
    started_at: Optional[str] = None
    finished_at: Optional[str] = None
    export_path: Optional[str] = None
    export_name: Optional[str] = None
    error: Optional[str] = None
    usage: Dict[str, int] = field(default_factory=dict)
    duration_seconds: Optional[float] = None
    source_files: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---------------------------------------------------------------------------
# Manager
# ---------------------------------------------------------------------------

class JobManager:
    def __init__(self, storage: Optional[StorageBackend] = None) -> None:
        self.settings = get_settings()
        self.storage = storage or get_storage()
        self._semaphore = asyncio.Semaphore(self.settings.max_concurrent_jobs)
        self._tasks: Dict[str, asyncio.Task] = {}
        self._loops: Dict[str, AgentLoop] = {}
        self._records: Dict[str, JobRecord] = {}
        self._lock = asyncio.Lock()
        self._persistence_path: Optional[Path] = None
        if self.settings.storage_backend == "local":
            # Persist job records on local disk for REST history after restart.
            self._persistence_path = Path(self.settings.storage_local_root) / "jobs.json"

    # ----- persistence -----
    async def load_persisted(self) -> None:
        if not self._persistence_path or not self._persistence_path.exists():
            return
        try:
            data = json.loads(self._persistence_path.read_text(encoding="utf-8"))
            for jid, rec in data.items():
                # Mark any running jobs as failed (process died).
                if rec.get("status") == JobStatus.RUNNING.value:
                    rec["status"] = JobStatus.FAILED.value
                    rec["error"] = "process restarted while running"
                    rec["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                self._records[jid] = JobRecord(**rec)
        except Exception as e:  # noqa: BLE001
            log.warning("could not load persisted jobs: %r", e)

    async def _persist(self) -> None:
        if not self._persistence_path:
            return
        async with self._lock:
            data = {jid: rec.to_dict() for jid, rec in self._records.items()}
        try:
            self._persistence_path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
        except Exception as e:  # noqa: BLE001
            log.warning("could not persist jobs: %r", e)

    # ----- public API -----
    async def create_job(self, spec: JobSpec) -> JobRecord:
        if spec.route.lower() not in self.settings.allowed_routes:
            raise ValueError(f"route '{spec.route}' not allowed (allowed: {self.settings.allowed_routes})")
        job_id = uuid.uuid4().hex
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        rec = JobRecord(
            job_id=job_id,
            status=JobStatus.QUEUED.value,
            spec=asdict(spec),
            created_at=now,
            source_files=list(spec.sources),
        )
        async with self._lock:
            self._records[job_id] = rec
        await self._persist()
        await bus.publish(Event(job_id=job_id, type=EventType.JOB_CREATED, data={"spec": asdict(spec)}))
        # Subscribe a webhook dispatcher for this job if URL configured
        wh_url = spec.webhook_url or self.settings.webhook_default_url
        if wh_url:
            asyncio.create_task(self._webhook_dispatcher(job_id, wh_url, spec.webhook_secret or self.settings.webhook_secret))
        # Launch the runner
        self._tasks[job_id] = asyncio.create_task(self._run_job(job_id, spec))
        return rec

    async def _run_job(self, job_id: str, spec: JobSpec) -> None:
        async with self._semaphore:
            rec = self._records.get(job_id)
            if not rec:
                return
            rec.status = JobStatus.RUNNING.value
            rec.started_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            await self._persist()
            try:
                # Stage source files into the agent's workdir (projects/<job_id>/sources/)
                await self._stage_sources(job_id, spec.sources)
                loop = AgentLoop(
                    job_id=job_id,
                    user_prompt=spec.prompt,
                    provider_override=spec.provider_override,
                )
                self._loops[job_id] = loop
                result = await asyncio.wait_for(loop.run(), timeout=self.settings.max_job_timeout_seconds)
                rec.usage = loop.usage
                if result.get("status") == "completed":
                    rec.status = JobStatus.COMPLETED.value
                    rec.export_path = result.get("export_path")
                    rec.export_name = Path(rec.export_path).name if rec.export_path else None
                    rec.duration_seconds = result.get("duration_seconds")
                elif result.get("status") == "cancelled":
                    rec.status = JobStatus.CANCELLED.value
                    rec.error = "cancelled"
                else:
                    rec.status = JobStatus.FAILED.value
                    rec.error = result.get("reason") or "agent failed"
            except asyncio.TimeoutError:
                rec.status = JobStatus.FAILED.value
                rec.error = f"timeout after {self.settings.max_job_timeout_seconds}s"
                await bus.publish(Event(job_id=job_id, type=EventType.JOB_FAILED, data={"error": rec.error}))
            except Exception as e:  # noqa: BLE001
                log.exception("job %s failed", job_id)
                rec.status = JobStatus.FAILED.value
                rec.error = f"{e!r}"
                await bus.publish(Event(job_id=job_id, type=EventType.JOB_FAILED, data={"error": str(e)}))
            finally:
                rec.finished_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                self._loops.pop(job_id, None)
                self._tasks.pop(job_id, None)
                await self._persist()

    async def _stage_sources(self, job_id: str, sources: List[str]) -> None:
        """Copy uploaded source files from storage into the agent's workdir
        so the LLM can read them. For local storage this is a no-op if the
        file already lives in the right place.
        """
        if not sources:
            return
        from app.pptmaster.runtime import get_runtime
        rt = get_runtime()
        workdir = rt.projects_dir / job_id / "sources"
        workdir.mkdir(parents=True, exist_ok=True)
        for src in sources:
            local = await self.storage.make_local_path(src)
            dest = workdir / Path(src).name
            if not Path(local).exists():
                log.warning("source %r not found at %r; skipping", src, local)
                continue
            if local != str(dest):
                Path(local).replace(dest) if Path(local).parent != dest.parent else None
                # Above branch is fragile; just copy to be safe.
                if not dest.exists():
                    dest.write_bytes(Path(local).read_bytes())

    async def cancel(self, job_id: str) -> bool:
        loop = self._loops.get(job_id)
        if loop:
            loop.request_stop()
            return True
        return False

    def get(self, job_id: str) -> Optional[JobRecord]:
        return self._records.get(job_id)

    def list_jobs(self, limit: int = 100) -> List[JobRecord]:
        return list(self._records.values())[-limit:]

    async def _webhook_dispatcher(self, job_id: str, url: str, secret: Optional[str]) -> None:
        """Subscribe to the bus for this job and POST each event to the webhook."""
        q = await bus.subscribe(job_id)
        try:
            while True:
                try:
                    ev = await asyncio.wait_for(q.get(), timeout=self.settings.max_job_timeout_seconds + 60)
                except asyncio.TimeoutError:
                    return
                await dispatch_event(url, ev.to_dict(), secret=secret)
                if ev.type in (EventType.JOB_COMPLETED, EventType.JOB_FAILED, EventType.JOB_CANCELLED):
                    return
        finally:
            await bus.unsubscribe(job_id, q)


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_manager: Optional[JobManager] = None


def get_job_manager() -> JobManager:
    global _manager
    if _manager is None:
        _manager = JobManager()
    return _manager

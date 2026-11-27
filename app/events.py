"""Typed event bus shared between agent loop, job manager, and API layer.

The job manager subscribes to these events for:
- persisting job state transitions
- dispatching webhook calls
- broadcasting to websocket clients

Three sinks all consume the same event stream:
  REST polling  -> /jobs/{id} reads the persisted event log
  WS streaming  -> /jobs/{id}/stream pushes events live as they arrive
  Webhook       -> POST events to a configurable URL
"""
from __future__ import annotations

import asyncio
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, AsyncIterator, Dict, List, Optional


class EventType(str, Enum):
    JOB_CREATED = "job.created"
    JOB_STARTED = "job.started"
    JOB_PROGRESS = "job.progress"
    JOB_TOOL_CALL = "job.tool_call"
    JOB_TOOL_RESULT = "job.tool_result"
    JOB_THOUGHT = "job.thought"          # free-form LLM assistant text chunk
    JOB_OUTLINE = "job.outline"          # structured content outline awaiting confirmation
    JOB_WARNING = "job.warning"
    JOB_COMPLETED = "job.completed"
    JOB_FAILED = "job.failed"
    JOB_CANCELLED = "job.cancelled"


class JobStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class Event:
    job_id: str
    type: EventType
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    data: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "job_id": self.job_id,
            "type": self.type.value,
            "timestamp": self.timestamp,
            "data": self.data,
        }


class EventBus:
    """Per-job pub/sub. Each job has its own queue; the API layer creates one
    when a WS client subscribes, and the job manager creates one when the job
    starts. Multiple subscribers per job are supported.
    """

    def __init__(self) -> None:
        # job_id -> list of subscriber queues
        self._subs: Dict[str, List[asyncio.Queue]] = {}
        # job_id -> persisted event log (for REST polling / late WS clients)
        self._logs: Dict[str, List[Event]] = {}
        self._lock = asyncio.Lock()

    async def subscribe(self, job_id: str) -> asyncio.Queue:
        async with self._lock:
            q: asyncio.Queue = asyncio.Queue(maxsize=1024)
            self._subs.setdefault(job_id, []).append(q)
            # Replay full history to the new subscriber so a reconnecting WS
            # client or a REST poller sees everything that has happened.
            for ev in self._logs.get(job_id, []):
                await q.put(ev)
        return q

    async def unsubscribe(self, job_id: str, q: asyncio.Queue) -> None:
        async with self._lock:
            if job_id in self._subs and q in self._subs[job_id]:
                self._subs[job_id].remove(q)

    async def publish(self, event: Event) -> None:
        async with self._lock:
            self._logs.setdefault(event.job_id, []).append(event)
            subs = list(self._subs.get(event.job_id, []))
        for q in subs:
            try:
                q.put_nowait(event)
            except asyncio.QueueFull:
                # Drop oldest to keep stream flowing; client can fall back
                # to REST polling for full history.
                try:
                    q.get_nowait()
                    q.put_nowait(event)
                except Exception:
                    pass

    def get_log(self, job_id: str) -> List[Event]:
        return list(self._logs.get(job_id, []))

    async def drain(self, job_id: str, q: asyncio.Queue, timeout: float = 1.0) -> AsyncIterator[Event]:
        """Yield events as they arrive. Used by the WS handler."""
        while True:
            try:
                ev = await asyncio.wait_for(q.get(), timeout=timeout)
                yield ev
            except asyncio.TimeoutError:
                # Allow the caller to break the loop between events.
                return


# Single process-wide instance. In a multi-worker deployment this would be
# replaced by Redis pub/sub, but in-process asyncio keeps the surface area
# small for the default deployment.
bus = EventBus()

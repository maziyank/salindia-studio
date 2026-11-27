"""Launches and tracks ppt-master's per-project live-preview editor.

ppt-master ships a Flask SVG editor at ``scripts/svg_editor/server.py`` that
serves a project's ``svg_output/`` over a loopback HTTP port and records its
pid + port in ``<project>/live_preview/lock.json``. We reuse it verbatim:

  * ``start(job_id)`` launches it in ``--live`` daemon mode for a build job's
    project directory (``--live`` creates ``svg_output/`` if the agent has not
    written a slide yet, so the preview can come up the moment a build starts).
  * the API layer reverse-proxies the editor under ``proxy_prefix(job_id)`` so
    the built-in web UI can embed it — the editor itself only listens on
    ``127.0.0.1`` and rejects non-loopback Host/Origin headers, which a remote
    browser could never satisfy directly.

The lock file is the source of truth: an editor started by a previous service
process is reused, and a stale lock (dead pid) is ignored.
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

from app.pptmaster.runtime import get_runtime

log = logging.getLogger("preview.manager")

_LAUNCH_TIMEOUT_SECONDS = 90


def _pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError:
        return False
    return True


class PreviewManager:
    def __init__(self) -> None:
        self._sessions: dict[str, int] = {}
        self._lock = asyncio.Lock()

    # ----- paths -----
    def _project_dir(self, job_id: str) -> Path:
        return get_runtime().projects_dir / job_id

    def _lock_files(self, job_id: str) -> list[Path]:
        project = self._project_dir(job_id)
        # Current runtime layout first, then the legacy root lock.
        return [
            project / "live_preview" / "lock.json",
            project / ".live_preview.lock",
        ]

    def proxy_prefix(self, job_id: str) -> str:
        """URL prefix (no trailing slash) the editor is reverse-proxied under."""
        return f"/jobs/{job_id}/preview"

    # ----- discovery -----
    def _read_port(self, job_id: str) -> Optional[int]:
        """Return the live editor's port from its lock, or None."""
        for lock_file in self._lock_files(job_id):
            try:
                data = json.loads(lock_file.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if not isinstance(data, dict):
                continue
            try:
                port = int(data.get("port") or 0)
                pid = int(data.get("pid") or 0)
            except (TypeError, ValueError):
                continue
            if port > 0 and _pid_alive(pid):
                return port
        return None

    def port(self, job_id: str) -> Optional[int]:
        """Return the running editor's port, validating against the lock."""
        port = self._read_port(job_id)
        if port is None:
            self._sessions.pop(job_id, None)
        else:
            self._sessions[job_id] = port
        return port

    def base_url(self, job_id: str) -> Optional[str]:
        port = self.port(job_id)
        return f"http://127.0.0.1:{port}" if port else None

    # ----- lifecycle -----
    async def start(self, job_id: str) -> Optional[int]:
        """Ensure a live-preview editor is running for this job. Idempotent.

        Returns the port, or None if the editor could not be started (e.g. the
        ppt-master runtime or Flask is unavailable).
        """
        async with self._lock:
            existing = self._read_port(job_id)
            if existing:
                self._sessions[job_id] = existing
                return existing

            rt = get_runtime()
            script = rt.preview_server_script
            if not script.is_file():
                log.warning("preview server script missing at %s", script)
                return None

            project = self._project_dir(job_id)
            try:
                project.mkdir(parents=True, exist_ok=True)
            except OSError as e:  # noqa: BLE001
                log.warning("cannot create project dir for preview %s: %r", job_id, e)
                return None

            cmd = [sys.executable, str(script), str(project), "--live", "--daemon", "--no-browser"]
            try:
                proc = await asyncio.to_thread(
                    subprocess.run, cmd, capture_output=True, text=True,
                    timeout=_LAUNCH_TIMEOUT_SECONDS,
                )
            except (OSError, subprocess.TimeoutExpired) as e:  # noqa: BLE001
                log.warning("preview launch failed for %s: %r", job_id, e)
                return None

            port = self._read_port(job_id)
            if not port:
                detail = (proc.stderr or proc.stdout or "").strip()[-500:]
                log.warning("preview did not report a port for %s (rc=%s): %s",
                            job_id, proc.returncode, detail)
                return None
            self._sessions[job_id] = port
            log.info("live preview ready for job %s at %s", job_id, self.base_url(job_id))
            return port

    async def stop(self, job_id: str) -> bool:
        """Stop the editor for this job (idempotent)."""
        rt = get_runtime()
        script = rt.preview_server_script
        project = self._project_dir(job_id)
        self._sessions.pop(job_id, None)
        if not script.is_file():
            return False
        cmd = [sys.executable, str(script), str(project), "--shutdown"]
        try:
            await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True, timeout=30,
            )
            return True
        except (OSError, subprocess.TimeoutExpired) as e:  # noqa: BLE001
            log.warning("preview stop failed for %s: %r", job_id, e)
            return False


_manager: Optional[PreviewManager] = None


def get_preview_manager() -> PreviewManager:
    global _manager
    if _manager is None:
        _manager = PreviewManager()
    return _manager

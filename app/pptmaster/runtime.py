"""Locate and (optionally) auto-provision the hugohe3/ppt-master repo.

On startup (if PPTMASTER_AUTO_SETUP=true) the service clones the repo into
PPTMASTER_REPO_DIR and runs `pip install -r requirements.txt`. After setup,
the runtime exposes canonical paths the agent loop uses:
  - skill_file:  <repo>/skills/ppt-master/SKILL.md
  - projects_dir:<repo>/projects/
  - exports_dir: <repo>/exports/
  - scripts_dir: <repo>/skills/ppt-master/scripts/

If the repo already exists, we do a `git pull` (best-effort) so updates are
picked up on container restart. Network failures are non-fatal: the service
boots anyway and surfaces the problem via /health, so a misconfigured offline
deployment doesn't just hang.
"""
from __future__ import annotations

import asyncio
import os
import shutil
import subprocess
from functools import lru_cache
from pathlib import Path
from typing import List, Optional

from app.config import get_settings


class PPTMasterRuntime:
    def __init__(self) -> None:
        s = get_settings()
        self.repo_dir = Path(s.pptmaster_repo_dir)
        self.repo_url = s.pptmaster_repo_url
        self.branch = s.pptmaster_repo_branch
        self.auto_setup = s.pptmaster_auto_setup
        self._ready = False
        self._last_error: Optional[str] = None

    # ----- paths -----
    @property
    def skill_file(self) -> Path:
        # The repo layout puts the skill under skills/ppt-master/SKILL.md
        return self.repo_dir / "skills" / "ppt-master" / "SKILL.md"

    @property
    def skill_dir(self) -> Path:
        return self.repo_dir / "skills" / "ppt-master"

    @property
    def scripts_dir(self) -> Path:
        return self.skill_dir / "scripts"

    @property
    def projects_dir(self) -> Path:
        return self.repo_dir / "projects"

    @property
    def exports_dir(self) -> Path:
        return self.repo_dir / "exports"

    @property
    def svg_final_dir(self) -> Path:
        return self.repo_dir / "svg_final"

    @property
    def is_ready(self) -> bool:
        return self._ready and self.skill_file.exists()

    @property
    def last_error(self) -> Optional[str]:
        return self._last_error

    # ----- provisioning -----
    def _run(self, cmd: List[str], cwd: Optional[Path] = None) -> subprocess.CompletedProcess:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=600)

    def _clone_or_pull(self) -> None:
        if self.repo_dir.exists() and (self.repo_dir / ".git").exists():
            # pull
            self._run(["git", "fetch", "--depth=1", "origin", self.branch], cwd=self.repo_dir)
            self._run(["git", "reset", "--hard", f"origin/{self.branch}"], cwd=self.repo_dir)
        else:
            if self.repo_dir.exists():
                shutil.rmtree(self.repo_dir, ignore_errors=True)
            self.repo_dir.parent.mkdir(parents=True, exist_ok=True)
            self._run([
                "git", "clone", "--depth=1", "--branch", self.branch, self.repo_url, str(self.repo_dir),
            ])

    def _install_deps(self) -> None:
        reqs = self.repo_dir / "requirements.txt"
        if not reqs.exists():
            return
        # `sys.executable` so we install into the same interpreter we run in
        py = os.sys.executable
        self._run([py, "-m", "pip", "install", "--no-input", "-r", str(reqs)])

    def setup(self) -> None:
        """Synchronous setup. Called from a thread executor at startup."""
        try:
            if self.auto_setup:
                self._clone_or_pull()
                self._install_deps()
            # Ensure working dirs exist
            for d in (self.projects_dir, self.exports_dir, self.svg_final_dir):
                d.mkdir(parents=True, exist_ok=True)
            self._ready = self.skill_file.exists()
            if not self._ready:
                self._last_error = (
                    f"SKILL.md not found at {self.skill_file}. "
                    f"Set PPTMASTER_AUTO_SETUP=true or point PPTMASTER_REPO_DIR at a checkout."
                )
        except subprocess.CalledProcessError as e:
            self._last_error = f"setup command failed: {e.stderr or e.stdout or e}"
        except Exception as e:  # noqa: BLE001
            self._last_error = f"setup error: {e!r}"

    async def setup_async(self) -> None:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.setup)

    # ----- skill loading -----
    def load_skill_md(self) -> str:
        """Return the contents of SKILL.md, which becomes the system prompt
        for the agent loop. The model needs the actual workflow rules.
        """
        if not self.skill_file.exists():
            raise FileNotFoundError(
                f"SKILL.md missing at {self.skill_file}. Run with PPTMASTER_AUTO_SETUP=true."
            )
        return self.skill_file.read_text(encoding="utf-8")


@lru_cache
def get_runtime() -> PPTMasterRuntime:
    return PPTMasterRuntime()

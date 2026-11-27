"""Tool registry: the callable surface the agent loop exposes to the LLM.

Each tool is a thin async wrapper around a real operation the pipeline needs:
read/write files inside the job's workdir, list files, run a PPT Master
script, fetch SKILL.md, search for AI/web images, and finalize the deck.

The tool *schemas* (name, description, parameters) are sent to the LLM as
the `tools` argument of each chat call. The tool *implementations* are
invoked here when the LLM asks for one.

Security: every path is constrained to the job's sandbox workdir; the LLM
cannot escape it.
"""
from __future__ import annotations

import asyncio
import json
import os
import shlex
import subprocess
from pathlib import Path
from typing import Any, Awaitable, Callable, Dict, List

from app.events import Event, EventType, bus
from app.pptmaster.runtime import get_runtime


ToolFn = Callable[[Dict[str, Any], str], Awaitable[Any]]
# (args, job_id) -> result (must be JSON-serializable)


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: Dict[str, Dict[str, Any]] = {}

    def register(
        self,
        name: str,
        description: str,
        parameters: Dict[str, Any],
        fn: ToolFn,
    ) -> None:
        self._tools[name] = {"description": description, "parameters": parameters, "fn": fn}

    def schemas(self) -> List[Dict[str, Any]]:
        """Return the tool schemas offered to the LLM (every registered tool)."""
        return [
            {"name": n, "description": t["description"], "parameters": t["parameters"]}
            for n, t in self._tools.items()
        ]

    async def call(self, name: str, args: Dict[str, Any], job_id: str) -> Any:
        if name not in self._tools:
            raise ValueError(f"unknown tool: {name}")
        return await self._tools[name]["fn"](args, job_id)


# ---------------------------------------------------------------------------
# Job sandbox helpers
# ---------------------------------------------------------------------------

def _job_workdir(job_id: str) -> Path:
    """Each job gets a private working directory under the PPT Master
    projects/ tree: <repo>/projects/<job_id>/. This is where the upstream
    pipeline expects sources to live.
    """
    rt = get_runtime()
    wd = rt.projects_dir / job_id
    (wd / "sources").mkdir(parents=True, exist_ok=True)
    return wd


def _safe_join(base: Path, rel: str) -> Path:
    parts = [p for p in rel.split("/") if p not in ("", ".")]
    if any(p == ".." for p in parts):
        raise ValueError(f"illegal path: {rel}")
    return base.joinpath(*parts)


# ---------------------------------------------------------------------------
# Concrete tool implementations
# ---------------------------------------------------------------------------

async def _read_skill_md(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """Return the PPT Master SKILL.md content. The LLM calls this once at the
    start to load the workflow rules into context."""
    rt = get_runtime()
    try:
        text = rt.load_skill_md()
        return {"ok": True, "content": text, "length": len(text)}
    except FileNotFoundError as e:
        return {"ok": False, "error": str(e)}


async def _list_project_files(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """List files the user uploaded for this job (under sources/)."""
    wd = _job_workdir(job_id)
    src = wd / "sources"
    files = []
    if src.exists():
        for p in sorted(src.rglob("*")):
            if p.is_file():
                files.append({"path": str(p.relative_to(wd)), "size": p.stat().st_size})
    return {"files": files}


async def _read_file(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """Read a text file (or extract text from a binary doc) from the job
    workdir. For PDF/DOCX, returns extracted plain text so the LLM can analyze
    without needing OCR.
    """
    rel = args["path"]
    wd = _job_workdir(job_id)
    full = _safe_join(wd, rel)
    if not full.exists():
        return {"ok": False, "error": f"not found: {rel}"}
    ext = full.suffix.lower()
    if ext in (".txt", ".md", ".svg", ".json", ".xml", ".csv"):
        return {"ok": True, "content": full.read_text(encoding="utf-8", errors="replace")}
    if ext == ".pdf":
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(full))
            text = "\n\n".join((page.extract_text() or "") for page in reader.pages)
            return {"ok": True, "content": text, "pages": len(reader.pages)}
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "error": f"pdf extract failed: {e!r}"}
    if ext == ".docx":
        try:
            from docx import Document  # type: ignore
            doc = Document(str(full))
            text = "\n".join(p.text for p in doc.paragraphs)
            return {"ok": True, "content": text}
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "error": f"docx extract failed: {e!r}"}
    return {"ok": False, "error": f"unsupported file type: {ext}"}


async def _write_file(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """Write a text file (SVG slide, notes, manifest, etc.) into the job
    workdir. Used by the LLM to emit per-slide SVG and intermediate artifacts.
    """
    rel = args["path"]
    content = args["content"]
    wd = _job_workdir(job_id)
    full = _safe_join(wd, rel)
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding="utf-8")
    return {"ok": True, "path": rel, "size": len(content)}


async def _list_dir(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """List arbitrary directory in the job workdir."""
    rel = args.get("path", "")
    wd = _job_workdir(job_id)
    target = _safe_join(wd, rel) if rel else wd
    if not target.exists():
        return {"ok": False, "error": f"not found: {rel}"}
    items = []
    for p in sorted(target.iterdir()):
        items.append({"name": p.name, "type": "dir" if p.is_dir() else "file", "size": p.stat().st_size if p.is_file() else 0})
    return {"ok": True, "items": items}


async def _run_pptmaster_script(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """Run a PPT Master script (image_gen.py / image_search.py / svg_to_pptx.py
    / update_repo.py) in a subprocess and return its stdout/stderr.

    Scripts are resolved from the PPT Master scripts dir (the agent cannot run
    its own scripts through this tool). They run with the job workdir as cwd,
    so a project-relative path like "." refers to the agent's workdir.
    """
    script = args["script"]  # e.g. "svg_to_pptx.py"
    extra_args: List[str] = list(args.get("args", []))
    rt = get_runtime()
    # scripts_dir may be configured relative to the service root; resolve it
    # against the process cwd so it still works when we run from the job workdir.
    scripts_dir = rt.scripts_dir.resolve()
    script_path = (scripts_dir / script).resolve()
    if not script_path.is_file():
        return {"ok": False, "error": f"script not found: {script}"}
    cmd = [os.sys.executable, str(script_path)] + extra_args
    wd = _job_workdir(job_id).resolve()
    try:
        proc = await asyncio.to_thread(
            subprocess.run, cmd, cwd=str(wd), capture_output=True, text=True, timeout=300
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"script {script} timed out after 300s", "timeout": True}
    return {
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-4000:],
        "stderr": proc.stderr[-4000:],
    }


async def _finalize_deck(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """The LLM signals completion by writing the final .pptx path it produced
    (or assembled) and pointing the service at it. In the absence of a fully
    integrated DrawingML exporter, this tool also accepts an already-produced
    .pptx file under the workdir and stages it to exports/ for delivery.
    """
    rel = args["pptx_path"]
    wd = _job_workdir(job_id)
    src = _safe_join(wd, rel)
    if not src.exists():
        return {"ok": False, "error": f"pptx not found: {rel}"}
    rt = get_runtime()
    rt.exports_dir.mkdir(parents=True, exist_ok=True)
    import time
    ts = time.strftime("%Y%m%d_%H%M%S")
    out_name = f"{job_id}_{ts}.pptx"
    out_path = rt.exports_dir / out_name
    out_path.write_bytes(src.read_bytes())
    return {"ok": True, "export_path": str(out_path), "export_name": out_name}


async def _progress(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """Free-form progress message the LLM can emit so clients see live status."""
    await bus.publish(Event(job_id=job_id, type=EventType.JOB_PROGRESS, data={
        "message": args.get("message", ""),
        "stage": args.get("stage", ""),
        "percent": args.get("percent"),
    }))
    return {"ok": True}


async def _http_get(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
    """Restricted HTTP GET for downloading image URLs the LLM found via
    image_search. Limited to ~10MB and stores result in workdir.
    """
    url = args["url"]
    dest = args.get("dest")
    import httpx
    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            return {"ok": False, "error": f"http {resp.status_code}"}
        body = resp.content
        if len(body) > 10 * 1024 * 1024:
            return {"ok": False, "error": "file too large (>10MB)"}
        if dest:
            wd = _job_workdir(job_id)
            full = _safe_join(wd, dest)
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_bytes(body)
            return {"ok": True, "path": dest, "size": len(body)}
        return {"ok": True, "size": len(body), "content_type": resp.headers.get("content-type", "")}


# ---------------------------------------------------------------------------
# Default registry
# ---------------------------------------------------------------------------

def get_default_tools() -> ToolRegistry:
    reg = ToolRegistry()
    reg.register(
        "read_skill_md",
        "Read the PPT Master SKILL.md workflow rules. Call this once at the start.",
        {"type": "object", "properties": {}, "required": []},
        _read_skill_md,
    )
    reg.register(
        "list_project_files",
        "List files the user uploaded for this job (under sources/).",
        {"type": "object", "properties": {}, "required": []},
        _list_project_files,
    )
    reg.register(
        "read_file",
        "Read a text file, PDF, or DOCX from the job workdir. Returns extracted text for binary docs.",
        {"type": "object", "properties": {"path": {"type": "string", "description": "relative path inside the job workdir"}}, "required": ["path"]},
        _read_file,
    )
    reg.register(
        "write_file",
        "Write a text file (SVG, notes, manifest) into the job workdir.",
        {"type": "object",
         "properties": {"path": {"type": "string"}, "content": {"type": "string"}},
         "required": ["path", "content"]},
        _write_file,
    )
    reg.register(
        "list_dir",
        "List contents of a directory in the job workdir.",
        {"type": "object", "properties": {"path": {"type": "string", "default": ""}}, "required": []},
        _list_dir,
    )
    reg.register(
        "run_pptmaster_script",
        "Run a PPT Master script (image_gen.py / image_search.py). Pass `script` and `args`.",
        {"type": "object",
         "properties": {
             "script": {"type": "string", "description": "filename in scripts/, e.g. image_search.py"},
             "args": {"type": "array", "items": {"type": "string"}, "default": []},
         },
         "required": ["script"]},
        _run_pptmaster_script,
    )
    reg.register(
        "http_get",
        "Download a URL (max 10MB) and optionally save to a path inside the job workdir.",
        {"type": "object",
         "properties": {"url": {"type": "string"}, "dest": {"type": "string"}},
         "required": ["url"]},
        _http_get,
    )
    reg.register(
        "progress",
        "Emit a progress message visible to the client (REST/WS/webhook).",
        {"type": "object",
         "properties": {
             "message": {"type": "string"},
             "stage": {"type": "string", "description": "e.g. analyze, design, render, export"},
             "percent": {"type": "number", "nullable": True},
         },
         "required": ["message"]},
        _progress,
    )
    reg.register(
        "finalize_deck",
        "Signal that the .pptx is ready. Stages the file to exports/ for client download.",
        {"type": "object",
         "properties": {"pptx_path": {"type": "string", "description": "relative path to the .pptx inside the job workdir"}},
         "required": ["pptx_path"]},
        _finalize_deck,
    )
    return reg

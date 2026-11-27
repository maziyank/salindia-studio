"""Engine-agnostic content-outline generation.

This phase is deliberately independent of any slide-rendering engine (PPT
Master or otherwise). It only:

  1. lists / reads the source files the user attached (straight from storage),
  2. asks the LLM for a structured content outline, and
  3. records that outline via `submit_outline`.

It never touches the PPT Master repo, its projects/ tree, SKILL.md, or any
build/export tooling. The approved outline is handed to the build phase later,
which is where a concrete rendering engine plugs in.
"""
from __future__ import annotations

import io
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.agent.tools import ToolRegistry
from app.events import Event, EventType, bus
from app.llm.base import LLMMessage, LLMProvider
from app.storage.base import StorageBackend


OUTLINE_SYSTEM_PROMPT = """You are the planning assistant of Salindia Studio. In
THIS phase your only job is to produce a CONTENT OUTLINE for a slide deck, then
stop.

Hard rules:
- Produce an outline only. Do NOT write or render slides, do NOT run any export
  or build tooling, and do NOT assume any particular presentation engine. The
  deck is built later, by a separate step, only after the user reviews and
  approves this outline.
- Inspect the material the user attached before outlining: call `list_sources`
  to see the available files, then `read_source` on the relevant ones.
- Base the structure on the user's request and the "Design spec requirements"
  embedded in it (slide count, tone, language, template). Honour the requested
  number of slides (default ~10) and the requested output language for every
  string.

When ready, call `submit_outline` EXACTLY ONCE with:
  - title: a concise, specific deck title
  - slides: an ordered array; each item is
      {"title": "...", "bullets": [...], "data": "...", "context": "..."}
Give every slide:
  - an assertion-style title (a claim, not a label);
  - 2-5 short bullets (<= 12 words each) as the slide's content;
  - `data`: the concrete supporting evidence - key facts, figures, dates,
    names, or quotations drawn from the attached material (one per line). Never
    invent a figure you cannot support; if the data is missing, state what
    should be gathered instead;
  - `context`: 1-3 sentences of background/rationale - why this slide exists,
    what it assumes, and how it connects to the neighbouring slides.
Cover the full arc: an opening, the body, and a closing slide. After
`submit_outline` returns, reply with a single short line and stop - do not
call any other tool.
"""


def _extract_text(name: str, data: bytes) -> Dict[str, Any]:
    """Return plain text for a source file so the LLM can analyze it without
    needing the original format. Mirrors the build-phase reader but works on
    in-memory bytes (sources come from storage, not a workdir)."""
    ext = Path(name).suffix.lower()
    if ext in (".txt", ".md", ".svg", ".json", ".xml", ".csv"):
        return {"ok": True, "content": data.decode("utf-8", errors="replace")}
    if ext == ".pdf":
        try:
            from pypdf import PdfReader
            reader = PdfReader(io.BytesIO(data))
            text = "\n\n".join((page.extract_text() or "") for page in reader.pages)
            return {"ok": True, "content": text, "pages": len(reader.pages)}
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "error": f"pdf extract failed: {e!r}"}
    if ext == ".docx":
        try:
            from docx import Document  # type: ignore
            doc = Document(io.BytesIO(data))
            text = "\n".join(p.text for p in doc.paragraphs)
            return {"ok": True, "content": text}
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "error": f"docx extract failed: {e!r}"}
    return {"ok": False, "error": f"unsupported file type: {ext}"}


def _as_str(value: Any) -> str:
    """Coerce a model-supplied field to a trimmed, newline-joined string."""
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return "\n".join(str(v).strip() for v in value if str(v).strip())
    return str(value).strip()


def _normalize_slide(item: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize one outline slide. `bullets` is the content; `data` and
    `context` carry the supporting evidence and rationale."""
    bullets = item.get("bullets") or []
    if isinstance(bullets, str):
        bullets = bullets.split("\n")
    return {
        "title": str(item.get("title", "")).strip(),
        "bullets": [str(b).strip() for b in bullets if str(b).strip()],
        "data": _as_str(item.get("data")),
        "context": _as_str(item.get("context")),
    }


def _normalize_outline(obj: Dict[str, Any]) -> Dict[str, Any]:
    obj = obj if isinstance(obj, dict) else {}
    raw = obj.get("slides")
    raw = raw if isinstance(raw, list) else []
    return {
        "title": str(obj.get("title", "")).strip(),
        "slides": [_normalize_slide(s) for s in raw if isinstance(s, dict)],
    }


def _parse_json_object(text: str) -> Dict[str, Any]:
    """Extract the first JSON object from a model reply, tolerating code
    fences and surrounding prose."""
    if not text:
        raise ValueError("empty model response")
    s = text.strip()
    if s.startswith("```"):
        parts = s.split("```")
        s = parts[1] if len(parts) >= 2 else s
        if s.lstrip().lower().startswith("json"):
            s = s.lstrip()[4:]
    start, end = s.find("{"), s.rfind("}")
    if start == -1 or end < start:
        raise ValueError("model did not return a JSON object")
    return json.loads(s[start:end + 1])


def get_outline_tools(storage: StorageBackend, sources: List[str]) -> ToolRegistry:
    """Build the minimal, engine-agnostic toolset for the outline phase.

    `sources` are logical storage paths (e.g. "<job_id>/sources/report.pdf").
    Nothing here depends on the rendering engine or its filesystem layout.
    """
    reg = ToolRegistry()
    source_set = list(sources)

    async def _list_sources(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
        files: List[Dict[str, Any]] = []
        for s in source_set:
            try:
                present = await storage.exists(s)
            except Exception:  # noqa: BLE001
                present = False
            if present:
                files.append({"path": s, "name": Path(s).name})
        return {"files": files}

    async def _read_source(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
        rel = str(args.get("path") or args.get("name") or "").strip()
        target = rel if rel in source_set else next(
            (s for s in source_set if Path(s).name == rel), ""
        )
        if not target:
            return {"ok": False, "error": f"not found: {rel!r}. Use `list_sources` first."}
        try:
            data = await storage.get(target)
        except Exception as e:  # noqa: BLE001
            return {"ok": False, "error": f"read failed: {e!r}"}
        return _extract_text(target, data)

    async def _submit_outline(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
        outline = _normalize_outline(args)
        slides = outline["slides"]
        await bus.publish(Event(job_id=job_id, type=EventType.JOB_OUTLINE, data={"outline": outline}))
        return {"ok": True, "outline": outline, "slide_count": len(slides)}

    async def _progress(args: Dict[str, Any], job_id: str) -> Dict[str, Any]:
        await bus.publish(Event(job_id=job_id, type=EventType.JOB_PROGRESS, data={
            "message": args.get("message", ""),
            "stage": args.get("stage", ""),
            "percent": args.get("percent"),
        }))
        return {"ok": True}

    reg.register(
        "list_sources",
        "List the source files the user attached to this job.",
        {"type": "object", "properties": {}, "required": []},
        _list_sources,
    )
    reg.register(
        "read_source",
        "Read an attached source file (text, PDF, or DOCX) as plain text. "
        "Pass the `path` (or `name`) returned by list_sources.",
        {"type": "object",
         "properties": {"path": {"type": "string", "description": "path or name of a source file"}},
         "required": ["path"]},
        _read_source,
    )
    reg.register(
        "submit_outline",
        "Submit the deck's content outline. Call once with a title and an ordered "
        "list of slides; the phase then ends for user review.",
        {"type": "object",
         "properties": {
             "title": {"type": "string", "description": "Deck title"},
             "slides": {
                 "type": "array",
                 "description": "Ordered slides; each has a title, short bullets, supporting data, and context.",
                 "items": {
                     "type": "object",
                     "properties": {
                         "title": {"type": "string", "description": "Assertion-style slide title"},
                         "bullets": {"type": "array", "items": {"type": "string"},
                                     "description": "2-5 short content bullets (<= 12 words each)"},
                         "data": {"type": "string",
                                  "description": "Supporting facts, figures, or evidence (one per line)"},
                         "context": {"type": "string",
                                     "description": "1-3 sentences of background/rationale for this slide"},
                     },
                     "required": ["title"],
                 },
             },
         },
         "required": ["title", "slides"]},
        _submit_outline,
    )
    reg.register(
        "progress",
        "Emit a short progress message visible to the client.",
        {"type": "object",
         "properties": {"message": {"type": "string"}, "stage": {"type": "string"}},
         "required": ["message"]},
        _progress,
    )
    return reg


# ---------------------------------------------------------------------------
# AI refinement of an already-generated outline
# ---------------------------------------------------------------------------

_REFINE_RULES = """Refinement rules:
- Turn each title into an assertion (a claim), not a label.
- Keep 2-5 bullets per slide, each <= 12 words.
- `data`: concrete supporting facts/figures/quotations. Never invent specific
  numbers, dates, or citations you cannot support; if the evidence is missing,
  say what should be gathered instead.
- `context`: 1-3 sentences of background/rationale for the slide.
- Preserve the deck's language and slide count; do not add, drop, or reorder
  slides (unless the user's extra instruction explicitly asks for it).
Return ONLY a JSON object - no prose, no markdown code fences."""

REFINE_SLIDE_SYSTEM_PROMPT = (
    "You are the planning assistant of Salindia Studio, refining ONE slide of "
    "an existing presentation outline so it is sharper and better supported. "
    "Return a single slide object.\n\n" + _REFINE_RULES
)

REFINE_OUTLINE_SYSTEM_PROMPT = (
    "You are the planning assistant of Salindia Studio, refining a full "
    "presentation outline for coherence and rigor while preserving the same "
    "number of slides and their order.\n\n" + _REFINE_RULES
)


def _refine_context(outline: Dict[str, Any], instruction: Optional[str]) -> str:
    parts = [
        "Deck title: " + (outline.get("title") or "(untitled)"),
        "",
        "Current outline (JSON):",
        json.dumps(outline, ensure_ascii=False, indent=2),
    ]
    if instruction:
        parts += ["", "Extra instruction from the user: " + instruction]
    return "\n".join(parts)


async def refine_slide(llm: LLMProvider, outline: Dict[str, Any], index: int,
                       instruction: Optional[str] = None) -> Dict[str, Any]:
    """Ask the LLM to improve the single slide at `index` (0-based)."""
    norm = _normalize_outline(outline or {})
    if index < 0 or index >= len(norm["slides"]):
        raise ValueError(f"slide index {index} out of range")
    user = (
        _refine_context(norm, instruction)
        + f"\n\nRefine ONLY slide index {index} (slide {index + 1} of {len(norm['slides'])})."
        + '\nReply with a JSON object: {"title": ..., "bullets": [...], "data": ..., "context": ...}'
    )
    resp = await llm.chat([LLMMessage(role="user", content=user)],
                          system=REFINE_SLIDE_SYSTEM_PROMPT)
    return _normalize_slide(_parse_json_object(resp.text))


async def refine_outline(llm: LLMProvider, outline: Dict[str, Any],
                         instruction: Optional[str] = None) -> Dict[str, Any]:
    """Ask the LLM to improve the whole outline."""
    norm = _normalize_outline(outline or {})
    user = (
        _refine_context(norm, instruction)
        + "\n\nRefine the WHOLE outline."
        + '\nReply with a JSON object: {"title": ..., "slides": [{"title": ..., '
        + '"bullets": [...], "data": ..., "context": ...}]}'
    )
    resp = await llm.chat([LLMMessage(role="user", content=user)],
                          system=REFINE_OUTLINE_SYSTEM_PROMPT)
    return _normalize_outline(_parse_json_object(resp.text))

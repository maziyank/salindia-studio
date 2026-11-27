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
THIS phase your only job is to produce a DETAILED, PER-SLIDE CONTENT OUTLINE for
a slide deck, then stop.

Hard rules:
- Produce an outline only. Do NOT write or render slides, do NOT run any export
  or build tooling, and do NOT assume any particular presentation engine. The
  deck is built later, by a separate step, only after the user reviews and
  approves this outline.
- Inspect the material the user attached before outlining: call `list_sources`
  to see the available files, then `read_source` on the relevant ones.
- Base the structure on the user's request and the "Design spec requirements"
  embedded in it (slide count, tone, language, template, story framework,
  audience, core message). Honour the requested number of slides (default ~10)
  and the requested output language for every string.
- If a story framework is specified, make the slide order follow its sections:
    * SCQA - Situation, Complication, Question, Answer: establish the shared
      context, expose the tension or gap, pose the key question, then answer it.
    * Pyramid Principle - main message/recommendation first, then 3-5
      supporting arguments, each backed by data and evidence (top-down).
    * PAS (Problem - Agitate - Solve) - name the audience's problem, show the
      cost of leaving it unsolved, then present the solution and action plan.
    * What - So What - Now What - the facts/findings, their implications, then
      the next steps or decisions.
    * Past - Present - Future - the journey so far, the current state and
      challenges, then the vision, targets, and roadmap.
    * HCCC (Hook - Context - Core Message - Call to Action) - grab attention,
      give brief context, land the core idea, then close with a concrete ask.
  If the user left the framework to the planner, choose the one that best fits
  the topic and audience, follow it, and state your choice in the first
  slide's `context`.
- Plan the deck as an ARGUMENT, not a list of topics. Every slide must move the
  audience from one belief to the next; if a slide does not change what the
  audience thinks, knows, or does, cut it or merge it. Group slides into 2-4
  named parts that mirror the framework sections.

For EACH slide, think like a presentation designer and fill EVERY field below.
A reader must be able to hand this outline to a designer and get the intended
deck without asking follow-up questions. Vague slides ("Overview", "Key
points", "Thank you") are not acceptable.

  - title: an assertion-style claim (a full sentence that states the point),
    never a label. It should be the takeaway a viewer reads first.
  - audience_move: "From <what they currently believe or feel> -> to <what they
    should believe or feel after this slide>". One sentence. This is the job
    of the slide.
  - relationships: how this slide's parts relate logically, naming both the
    relation and the units, e.g. "link: claim -> three proofs", "order: step 1
    -> 2 -> 3", "contrast: before <-> after", "membership: four costs of one
    decision", "parent: category -> sub-items". Rigorous structure lives here.
  - layout: the composition / layout pattern in plain language, including
    where the eye lands first, e.g. "full-bleed photo; title and three figures
    over the darkest lower third", "two columns: diagram left, four bullets
    right", "hero number centred, one support line, source line at the foot".
  - core_message: the single sentence a viewer must remember from this slide.
    Specific and defensible, not a restatement of the title.
  - bullets: 3-6 on-slide content lines (<= 14 words each). These are the words
    that actually appear on the slide, not speaker notes. Use the source's
    concrete facts; no filler.
  - data: the concrete evidence behind the slide - key figures, dates, names,
    quotations, units and years, one per line. Cite the source or fact id when
    the material provides one. Never invent a figure; if the evidence is
    missing, state what must be gathered instead.
  - visualization: the visual form that carries the message - e.g. "horizontal
    bar chart, 5 categories, one highlighted", "timeline with 4 milestones",
    "2x2 matrix", "annotated diagram", "comparison table", "big-number
    callout", "none (text-led)". Name the axes, categories or annotations.
  - images: the imagery the slide needs - subject, framing and role
    (hero / background / support / icon), or "none". Respect the design spec's
    image strategy.
  - motion: an optional transition or build that reinforces the logic, e.g.
    "reveal the three proofs one at a time", "morph the chapter rail from the
    previous slide", or "none".
  - context: 1-3 sentences of background/rationale - why this slide exists,
    what it assumes, and how it connects to the neighbouring slides.

Also give the deck:
  - title: a concise, specific deck title.
  - narrative: one paragraph (3-5 sentences) describing the through-line - the
    argument arc, the turning points, and the closing ask.
  - parts: 2-4 short part names that group the slides (e.g. "Part 1: The old
    world").

Cover the full arc: an opening, the body, and a closing slide. When ready, call
`submit_outline` EXACTLY ONCE with `title`, `narrative`, `parts` and `slides`
(each slide carrying all the fields above). After `submit_outline` returns,
reply with a single short line and stop - do not call any other tool.
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
    """Normalize one outline slide into the detailed per-slide contract.

    `bullets` are the words that appear on the slide; `data` is the evidence;
    `audience_move`, `relationships`, `layout`, `core_message`, `visualization`,
    `images`, `motion` and `context` describe the design intent behind it."""
    bullets = item.get("bullets") or []
    if isinstance(bullets, str):
        bullets = bullets.split("\n")
    return {
        "title": str(item.get("title", "")).strip(),
        "audience_move": _as_str(item.get("audience_move")),
        "relationships": _as_str(item.get("relationships")),
        "layout": _as_str(item.get("layout")),
        "core_message": _as_str(item.get("core_message")),
        "bullets": [str(b).strip() for b in bullets if str(b).strip()],
        "data": _as_str(item.get("data")),
        "visualization": _as_str(item.get("visualization")),
        "images": _as_str(item.get("images")),
        "motion": _as_str(item.get("motion")),
        "context": _as_str(item.get("context")),
    }


def _normalize_outline(obj: Dict[str, Any]) -> Dict[str, Any]:
    obj = obj if isinstance(obj, dict) else {}
    raw = obj.get("slides")
    raw = raw if isinstance(raw, list) else []
    parts = obj.get("parts") or []
    if isinstance(parts, str):
        parts = [parts]
    return {
        "title": str(obj.get("title", "")).strip(),
        "narrative": _as_str(obj.get("narrative")),
        "parts": [str(p).strip() for p in parts if str(p).strip()],
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
        "Submit the deck's detailed content outline. Call once with a deck title, "
        "a narrative, 2-4 part names, and an ordered list of slides; the phase then "
        "ends for user review.",
        {"type": "object",
         "properties": {
             "title": {"type": "string", "description": "Concise, specific deck title"},
             "narrative": {"type": "string",
                           "description": "One paragraph (3-5 sentences) on the deck's through-line: the argument arc, turning points, and closing ask"},
             "parts": {"type": "array", "items": {"type": "string"},
                       "description": "2-4 short part names that group the slides"},
             "slides": {
                 "type": "array",
                 "description": "Ordered slides; each is a fully specified beat of the argument.",
                 "items": {
                     "type": "object",
                     "properties": {
                         "title": {"type": "string",
                                   "description": "Assertion-style claim (a full sentence stating the point), never a label"},
                         "audience_move": {"type": "string",
                                           "description": "From <current belief/feeling> -> to <intended belief/feeling>; the job of this slide"},
                         "relationships": {"type": "string",
                                           "description": "Logical relation between the slide's parts, naming the relation and the units, e.g. 'link: claim -> three proofs', 'order: step 1 -> 2 -> 3', 'contrast: before <-> after', 'membership: four costs of one decision'"},
                         "layout": {"type": "string",
                                    "description": "Composition / layout pattern in plain language, including where the eye lands first"},
                         "core_message": {"type": "string",
                                          "description": "The single sentence a viewer must remember from this slide"},
                         "bullets": {"type": "array", "items": {"type": "string"},
                                     "description": "3-6 on-slide content lines (<= 14 words each); the words that actually appear on the slide"},
                         "data": {"type": "string",
                                  "description": "Concrete evidence behind the slide - figures, dates, names, quotations, units, years - one per line; cite the source or fact id, never invent a figure"},
                         "visualization": {"type": "string",
                                           "description": "Visual form that carries the message (chart, timeline, matrix, diagram, table, big-number callout, or 'none (text-led)'), naming axes/categories/annotations"},
                         "images": {"type": "string",
                                    "description": "Imagery needed: subject, framing and role (hero / background / support / icon), or 'none'; respect the design spec's image strategy"},
                         "motion": {"type": "string",
                                    "description": "Optional transition or build that reinforces the logic, or 'none'"},
                         "context": {"type": "string",
                                     "description": "1-3 sentences of background/rationale: why this slide exists, what it assumes, how it connects to its neighbours"},
                     },
                     "required": ["title", "core_message", "bullets"],
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

_SLIDE_JSON_HINT = (
    '{"title": ..., "audience_move": ..., "relationships": ..., "layout": ..., '
    '"core_message": ..., "bullets": [...], "data": ..., "visualization": ..., '
    '"images": ..., "motion": ..., "context": ...}'
)

_REFINE_RULES = """Refinement rules:
- Keep every slide fully specified. Each slide must carry ALL of these fields, and
  none may be left as a vague placeholder:
    * title - an assertion (a full sentence stating the point), never a label.
    * audience_move - "From <current belief/feeling> -> to <intended belief/feeling>".
    * relationships - the logical relation between the slide's parts, naming the
      relation and the units (link / order / contrast / membership / parent / ...).
    * layout - the composition in plain language, including where the eye lands first.
    * core_message - the one sentence a viewer must remember from this slide.
    * bullets - 3-6 on-slide content lines (<= 14 words each), the words that
      actually appear on the slide.
    * data - concrete evidence (figures, dates, names, quotations, units, years),
      one per line. Never invent specific numbers, dates, or citations you cannot
      support; if the evidence is missing, say what should be gathered instead.
    * visualization - the visual form that carries the message (chart, timeline,
      matrix, diagram, table, big-number callout, or "none (text-led)"), naming
      axes/categories/annotations.
    * images - subject, framing and role (hero / background / support / icon), or
      "none".
    * motion - an optional transition/build that reinforces the logic, or "none".
    * context - 1-3 sentences of background/rationale and how the slide connects
      to its neighbours.
- Make the deck read as an argument: sharpen the audience_move and relationships
  so each slide earns its place and hands off to the next.
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
        + "\nReply with a JSON object holding every slide field: " + _SLIDE_JSON_HINT
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
        + '\nReply with a JSON object: {"title": ..., "narrative": ..., "parts": [...], '
        + '"slides": [' + _SLIDE_JSON_HINT + ', ...]}'
    )
    resp = await llm.chat([LLMMessage(role="user", content=user)],
                          system=REFINE_OUTLINE_SYSTEM_PROMPT)
    return _normalize_outline(_parse_json_object(resp.text))

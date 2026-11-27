"""Agent loop: the orchestration that turns a job prompt into PPT output.

Flow:
  1. Compose system prompt = SKILL.md + agent role instructions + job context.
  2. Send initial user message ("Create a PPT from sources/...") + tool schemas.
  3. If the LLM returns tool_use blocks, execute each tool, append the result
     as a `tool` message, and loop back to step 2.
  4. If the LLM returns text only (stop_reason == "stop") and the deck is
     finalized, the job is done.
  5. Enforce a hard iteration cap (LLM_MAX_ITERATIONS) to bound cost.

The loop emits an event for every assistant text chunk, every tool call,
and every tool result. The job manager listens to these for state updates;
the API layer relays them to WS clients and webhooks.

Cancellation: the loop checks `should_stop` between iterations. If set
(by the job manager on cancel), it aborts cleanly.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
import uuid
from typing import Any, Dict, List, Optional

from app.agent.outline import OUTLINE_SYSTEM_PROMPT
from app.agent.tools import ToolRegistry, get_default_tools
from app.config import get_settings
from app.events import Event, EventType, bus
from app.llm.base import LLMContent, LLMMessage, LLMProvider
from app.llm.factory import get_llm
from app.pptmaster.runtime import get_runtime

log = logging.getLogger("agent.loop")


SYSTEM_PREAMBLE = """You are the brain of a Salindia Studio. You drive the
hugohe3/ppt-master pipeline by calling tools. You NEVER write to the
filesystem directly; you ALWAYS use the provided tools.

Workflow rules are in the PPT Master SKILL.md. Call `read_skill_md` first to
load them, then follow them strictly.

Operating principles:
- Each job has a private workdir under projects/<job_id>/; sources the user
  uploaded are in sources/. You write intermediate files (SVG, notes, manifest)
  anywhere under the workdir.
- When you need an image, call `generate_image` with a detailed prompt (it uses
  the configured backend and saves to `images/<slug>.png`), or `run_pptmaster_script`
  with image_search.py, or `http_get` to fetch a URL.
- Emit progress regularly via the `progress` tool so the client can see status.
- Uploaded sources live at `sources/<filename>` inside your workdir. Read them
  with `read_file`; do not assume they are anywhere else.
- Your workdir is already a PPT Master project directory. Every script runs with
  your workdir as the working directory, so always pass "." as the project:
    1. design_spec.md — write it with `write_file`. This is the deck's full design
       contract and must be as detailed as the reference specs in
       ppt-master-examples. Open with `<!-- ppt-master-schema: design-spec/v1 -->`
       and a `# <project> - Design Spec` title, then include ALL of these
       sections, filled in for THIS deck (no placeholders):
         ## I. Project Information — a table of: project name, canvas format,
           page count, primary language, target audience (prose: who they are,
           what they already believe, what they need), communication intent,
           desired audience outcome, core message / ask / action, delivery
           context, artifact afterlife, reading mode, content strategy, design
           style, AI image acquisition path, generation mode, spec refinement,
           speaker notes (yes/no), custom animations, narration audio, created
           date. Add a Template Application paragraph: which layout prototypes
           this deck borrows, what may change, and why.
         ## II. Canvas Specification — format, dimensions, viewBox, margins,
           content area.
         ## III. Visual Theme — Theme Style (mode, mode references, mode
           behaviour, visual style, visual-style references, visual-style
           behaviour, theme, tone), a Color Scheme table with 10-12 roles
           (Role | HEX | Purpose: background, secondary background, primary,
           accent, secondary accent, body text, secondary text, divider, scrim,
           surface, ...), and an AI Image Strategy (image rendering, references,
           behaviour, visual, mood).
         ## IV. Typography System — a Font Plan table
           (Role | Character (Reference) | Primary | English if non-English |
           Fallback tail) covering title, body, display, chapter title, chapter
           number, quote and hero number; the per-role font stacks; a Role
           rationale; and a Font Size Hierarchy table (Purpose | Anchor Size px).
         ## V. Layout Principles — deck-wide direction: hierarchy direction,
           composition tendency, cross-page continuity, spacing posture, and
           spacing anchors (page margin, block gap, column gutter, corner radius,
           body leading). State the grid and how pages vary around it.
         ## VI. Icon Usage Specification — primary bundled library, stroke
           width, and a table of Icon Path | Suitable Scenarios (or an explicit
           "none" rationale).
         ## VII. Visualization Reference List — the chart/diagram families this
           deck uses and when.
         ## VIII. Image Resource List — a table with columns Filename |
           Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy |
           Acquire Via | Status | Reference | text_policy | page_role (or an
           explicit "no image resource is planned" rationale).
         ## IX. Content Outline — the approved per-slide outline, grouped into
           parts, with each slide's audience move, relationships, composition,
           title, core message, content, images, motion and fact ids.
         ## X. Speaker Notes Requirements — generation, filename, content, total
           duration, notes style, presentation purpose.
         ## XI. Technical Constraints Reminder — the hard rules that must hold
           when the slides are rendered.
       Keep it consistent with spec_lock.md below (same palette, fonts, canvas).
    2. spec_lock.md — write it with `write_file` in EXACTLY this Markdown lock
       dialect (## section, then "- key: value" lines). Do not use YAML/nesting:
         <!-- ppt-master-schema: spec-lock/v1 -->
         # Execution Lock
         ## canvas
         - viewBox: 0 0 1280 720
         - format: ppt169
         ## communication
         - primary_language: id-ID      # BCP-47 tag, NOT a language name
         - audience: ...
         - objective: ...
         - core_message: ...
         - consumption_mode: presentation
         ## mode
         - mode: instructional
         ## visual_style
         - visual_style: ...
         ## colors
         - bg: "#FFF8EE"
         - primary: "#10243E"
         - accent: "#FF6B5E"
         - text: "#17324D"
         ## typography
         - font_family: Arial
         - title_family: Arial
         - body_family: Arial
         - body: 22
         - title: 52
         ## icons
         - library: none
         - inventory: none
         ## page_rhythm
         - P01: anchor   (one line per page)
         ## pptx_structure
         - mode: flat
    3. Write slides as `svg_output/slide_01.svg`, `slide_02.svg`, … (1 file/page).
    4. run_pptmaster_script(script="svg_quality_checker.py", args=[".", "--stage", "final"])
       — must pass; the exporter refuses to run without a passing report.
    5. run_pptmaster_script(script="svg_to_pptx.py", args=["."]) — takes the
       project directory, not individual SVG files. It writes the .pptx into
       your workdir.
  Do not invent your own export script. This tool only runs scripts from the PPT
  Master scripts directory — you cannot run arbitrary Python through it; use
  `write_file` for files.
- When the .pptx exists, call `finalize_deck` with its relative path. That
  stages it for client download and ends the job. A job that ends without
  calling `finalize_deck` is a FAILURE, so never stop before finalizing.
- Be terse in your reasoning text; the client sees it live. Put detailed
  thinking into tool calls, not chat.
- If something fails, retry with a fix and keep going until the deck is
  finalized. Only emit a `progress` message with stage="error" if you are
  truly blocked (e.g. a required tool is unavailable) — and still do not end
  the turn without an explicit explanation of what is blocking you.
"""


class AgentLoop:
    def __init__(
        self,
        job_id: str,
        user_prompt: str,
        *,
        provider: Optional[LLMProvider] = None,
        tools: Optional[ToolRegistry] = None,
        max_iterations: Optional[int] = None,
        provider_override: Optional[str] = None,
        outline_only: bool = False,
    ) -> None:
        self.job_id = job_id
        self.user_prompt = user_prompt
        self.outline_only = outline_only
        self.settings = get_settings()
        self.llm: LLMProvider = provider or get_llm(override=provider_override)
        self.tools: ToolRegistry = tools or get_default_tools()
        self.max_iter = max_iterations or self.settings.llm_max_iterations
        self._should_stop = False
        self._messages: List[LLMMessage] = []
        self._total_input_tokens = 0
        self._total_output_tokens = 0
        self._tool_call_count = 0
        self._final_export: Optional[str] = None
        self._outline: Optional[Dict[str, Any]] = None
        self._nudged = False

    def request_stop(self) -> None:
        self._should_stop = True

    @property
    def usage(self) -> Dict[str, int]:
        return {
            "input_tokens": self._total_input_tokens,
            "output_tokens": self._total_output_tokens,
            "tool_calls": self._tool_call_count,
            "iterations": len([m for m in self._messages if m.role == "assistant"]),
        }

    @property
    def final_export(self) -> Optional[str]:
        return self._final_export

    @property
    def outline(self) -> Optional[Dict[str, Any]]:
        return self._outline

    async def _emit(self, etype: EventType, data: Dict[str, Any]) -> None:
        await bus.publish(Event(job_id=self.job_id, type=etype, data=data))

    async def _execute_tool(self, call: LLMContent) -> str:
        """Run a single tool call and return the stringified result for the
        next LLM turn. Catches all exceptions so a tool failure becomes a
        recoverable error message rather than crashing the loop."""
        name = call.tool_name or ""
        args = call.tool_args or {}
        await self._emit(EventType.JOB_TOOL_CALL, {"name": name, "args": args, "id": call.tool_call_id})
        self._tool_call_count += 1
        try:
            result = await self.tools.call(name, args, self.job_id)
            # Capture finalize_deck's export path for the job manager.
            if name == "finalize_deck" and isinstance(result, dict) and result.get("ok"):
                self._final_export = result.get("export_path")
                await self._emit(EventType.JOB_PROGRESS, {
                    "stage": "finalize", "message": "Deck finalized",
                    "export_name": result.get("export_name"),
                })
            # Capture the structured outline produced during the outline phase.
            # The tool itself publishes the JOB_OUTLINE event; here we just keep
            # a copy so run() can end the phase cleanly.
            if name == "submit_outline" and isinstance(result, dict) and result.get("outline"):
                self._outline = result.get("outline")
            payload = json.dumps(result, default=str, ensure_ascii=False)
            # Truncate huge tool outputs to keep context manageable
            if len(payload) > 8000:
                payload = payload[:8000] + "...[truncated]"
            await self._emit(EventType.JOB_TOOL_RESULT, {
                "id": call.tool_call_id, "name": name,
                "ok": bool(isinstance(result, dict) and result.get("ok", True)),
                "result": payload,
            })
            return payload
        except Exception as e:  # noqa: BLE001
            err = f"tool error: {name}: {e!r}"
            log.warning("tool %s failed: %r", name, e)
            await self._emit(EventType.JOB_WARNING, {"tool": name, "error": str(e)})
            return json.dumps({"ok": False, "error": err})

    def _nudge_text(self) -> str:
        if self.outline_only:
            return (
                "You ended your turn without calling `submit_outline`. The outline "
                "is not ready yet. Call `submit_outline` now with the deck title and "
                "the ordered list of slides, then stop. Do not reply with text only."
            )
        return (
            "You ended your turn without calling any tool, but the deck has "
            "not been finalized. Continue working now: use tools to produce "
            "the .pptx and call `finalize_deck` with its relative path. "
            "Do not reply with text only."
        )

    async def _finish_outline(self, started: float, iteration: int) -> Dict[str, Any]:
        """Emit completion for the outline phase and return the run summary."""
        await self._emit(EventType.JOB_COMPLETED, {
            "outline": self._outline,
            "duration_seconds": round(time.time() - started, 2),
            "usage": self.usage,
        })
        return {"status": "completed", "outline": self._outline,
                "iteration": iteration, "usage": self.usage}

    async def run(self) -> Dict[str, Any]:
        """Main loop. Returns a summary dict. Throws on unrecoverable errors."""
        started = time.time()
        await self._emit(EventType.JOB_STARTED, {"provider": self.llm.name, "prompt": self.user_prompt[:500]})

        # Seed the conversation
        self._messages.append(LLMMessage(role="user", content=self.user_prompt))

        if self.outline_only:
            # Standalone planning phase: no rendering engine involved. The
            # toolset was supplied by the caller (app.agent.outline) and already
            # contains only source-inspection + submit_outline tools.
            system = OUTLINE_SYSTEM_PROMPT
            tool_schemas = self.tools.schemas()
        else:
            # Build phase: drive the rendering engine (PPT Master). Append
            # SKILL.md to the system prompt when the runtime is ready; loading
            # here saves one round-trip (the LLM can still call read_skill_md).
            system = SYSTEM_PREAMBLE
            rt = get_runtime()
            if rt.is_ready:
                try:
                    system = SYSTEM_PREAMBLE + "\n\n--- SKILL.md ---\n\n" + rt.load_skill_md()
                except Exception as e:  # noqa: BLE001
                    log.warning("could not inline SKILL.md: %r", e)
            tool_schemas = self.tools.schemas()

        for iteration in range(1, self.max_iter + 1):
            if self._should_stop:
                await self._emit(EventType.JOB_CANCELLED, {"reason": "stop requested", "iteration": iteration})
                return {"status": "cancelled", "iteration": iteration, "usage": self.usage}

            try:
                resp = await self.llm.chat(
                    self._messages,
                    system=system,
                    tools=tool_schemas,
                    temperature=self.settings.llm_temperature,
                    max_tokens=self.settings.llm_max_tokens,
                )
            except Exception as e:  # noqa: BLE001
                log.exception("LLM call failed")
                await self._emit(EventType.JOB_FAILED, {"error": f"LLM error: {e!r}", "iteration": iteration})
                raise

            self._total_input_tokens += resp.usage_input_tokens
            self._total_output_tokens += resp.usage_output_tokens

            # Surface running token usage so clients can show live cost
            await self._emit(EventType.JOB_PROGRESS, {"usage": self.usage})

            # Surface assistant text as a thought event
            if resp.text:
                await self._emit(EventType.JOB_THOUGHT, {"text": resp.text, "iteration": iteration})

            # Append assistant turn
            self._messages.append(LLMMessage(role="assistant", content=resp.content))

            # If there are no tool calls, the LLM is done talking. If the deck
            # was finalized, great; otherwise consider it a soft failure.
            if not resp.tool_calls:
                # Outline phase: a submitted outline is the success condition.
                if self.outline_only and self._outline is not None:
                    return await self._finish_outline(started, iteration)
                if self._final_export:
                    await self._emit(EventType.JOB_COMPLETED, {
                        "export_path": self._final_export,
                        "duration_seconds": round(time.time() - started, 2),
                        "usage": self.usage,
                    })
                    return {"status": "completed", "export_path": self._final_export,
                            "iteration": iteration, "usage": self.usage}
                # No tool calls and no finalize. Give the model one chance to
                # correct itself before declaring failure, since a turn with
                # text but no tool call usually just means it lost the thread.
                if not self._nudged:
                    self._nudged = True
                    await self._emit(EventType.JOB_THOUGHT, {
                        "text": "Deck is not finalized yet; reminding the model to continue.",
                        "iteration": iteration,
                    })
                    self._messages.append(LLMMessage(role="user", content=self._nudge_text()))
                    continue
                await self._emit(EventType.JOB_FAILED, {
                    "error": "agent ended without calling finalize_deck",
                    "iteration": iteration,
                    "last_text": resp.text[:500],
                })
                return {"status": "failed", "reason": "no_finalize", "iteration": iteration, "usage": self.usage}

            # Execute each tool call and append tool result messages
            for call in resp.tool_calls:
                if self._should_stop:
                    break
                result_str = await self._execute_tool(call)
                self._messages.append(LLMMessage(
                    role="tool",
                    content=result_str,
                    tool_call_id=call.tool_call_id,
                    name=call.tool_name,
                ))
                # Outline phase ends as soon as the outline has been submitted;
                # no need to spend another LLM round-trip.
                if self.outline_only and self._outline is not None:
                    return await self._finish_outline(started, iteration)

        # Hit iteration cap
        await self._emit(EventType.JOB_FAILED, {
            "error": f"exceeded max iterations ({self.max_iter})",
            "usage": self.usage,
        })
        return {"status": "failed", "reason": "max_iterations", "usage": self.usage}

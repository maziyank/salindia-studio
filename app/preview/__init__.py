"""Live-preview subsystem.

Wraps ppt-master's own SVG live-preview editor (scripts/svg_editor/server.py)
so a build job's slides can be viewed/annotated while they are generated. The
editor binds to loopback only; this package both launches it and describes the
reverse-proxy prefix the API layer serves it under.
"""
from app.preview.manager import PreviewManager, get_preview_manager

__all__ = ["PreviewManager", "get_preview_manager"]

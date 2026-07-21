"""
Frame renderer.

Render text inside a simple frame.
"""

from __future__ import annotations

from typing import Any

from .box import BoxRenderer
from ..styles.rounded import BorderStyle, ROUNDED


class FrameRenderer(BoxRenderer):
    """Renderer for framed text."""

    def __init__(self, style: BorderStyle = ROUNDED):
        super().__init__(style=style)


_renderer = FrameRenderer()


def frame(value: Any, **kwargs) -> None:
    """
    Print a framed representation of a value.

    Examples
    --------
    >>> frame("Application Started")
    ╭─────────────────────────╮
    │ Application Started     │
    ╰─────────────────────────╯
    """
    _renderer.print(value, **kwargs)


def render_frame(value: Any, **kwargs) -> str:
    """
    Return the rendered frame without printing.
    """
    return _renderer.render(value, **kwargs)

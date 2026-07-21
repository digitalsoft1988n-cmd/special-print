"""
Box renderer.

Render text inside a bordered box.
"""

from __future__ import annotations

from typing import Any

from ..core.renderer import Renderer
from ..helpers.text import (
    measure_width,
    normalize_lines,
    pad_line,
    to_text,
)
from ..styles import BorderStyle, ROUNDED


class BoxRenderer(Renderer):
    """Renderer for boxed text."""

    def __init__(self, style: BorderStyle = ROUNDED):
        self.default_style = style

    def render(
        self,
        value: Any,
        *,
        style: BorderStyle | None = None,
        padding: int = 1,
        **kwargs,
    ) -> str:
        """
        Render a value inside a bordered box.

        Parameters
        ----------
        value:
            Object to render.

        style:
            Border style to use.

        padding:
            Horizontal padding inside the box.

        Returns
        -------
        str
            Rendered box.
        """
        style = style or self.default_style

        text = to_text(value)
        lines = normalize_lines(text)

        width = measure_width(lines)
        inner_width = width + (padding * 2)

        top = (
            f"{style.top_left}" f"{style.horizontal * inner_width}" f"{style.top_right}"
        )

        bottom = (
            f"{style.bottom_left}"
            f"{style.horizontal * inner_width}"
            f"{style.bottom_right}"
        )

        body = []

        for line in lines:
            body.append(
                f"{style.vertical}"
                f"{' ' * padding}"
                f"{pad_line(line, width)}"
                f"{' ' * padding}"
                f"{style.vertical}"
            )

        return "\n".join([top, *body, bottom])


_renderer = BoxRenderer()


def render_box(
    value: Any,
    *,
    style: BorderStyle = ROUNDED,
    padding: int = 1,
) -> str:
    """
    Render a box without printing it.
    """
    return _renderer.render(
        value,
        style=style,
        padding=padding,
    )


def box(
    value: Any,
    *,
    style: BorderStyle = ROUNDED,
    padding: int = 1,
) -> None:
    """
    Print a value inside a bordered box.

    Examples
    --------
    >>> box("Hello")

    >>> box("Hello", padding=3)
    """
    _renderer.print(
        value,
        style=style,
        padding=padding,
    )

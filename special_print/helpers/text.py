"""
Text utility functions used by renderers.
"""

from __future__ import annotations

from textwrap import wrap
from typing import List


def normalize_lines(text: str) -> List[str]:
    """
    Split text into individual lines.

    Empty input returns a single empty line.
    """
    if not text:
        return [""]

    return text.splitlines() or [""]


def measure_width(lines: List[str]) -> int:
    """
    Return the width of the longest line.
    """
    if not lines:
        return 0

    return max(len(line) for line in lines)


def pad_line(line: str, width: int) -> str:
    """
    Pad a line with spaces to match the desired width.
    """
    return line.ljust(width)


def wrap_lines(text: str, width: int) -> List[str]:
    """
    Wrap text to the specified width.
    """
    wrapped: List[str] = []

    for line in normalize_lines(text):
        if not line:
            wrapped.append("")
            continue

        wrapped.extend(wrap(line, width=width) or [""])

    return wrapped


def to_text(value: object) -> str:
    """
    Convert any Python object to its string representation.
    """
    return str(value)

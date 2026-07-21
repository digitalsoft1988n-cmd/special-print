"""
Rounded Unicode border style.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BorderStyle:
    """Represents a set of border characters."""

    top_left: str
    top_right: str
    bottom_left: str
    bottom_right: str

    horizontal: str
    vertical: str

    left_t: str
    right_t: str
    top_t: str
    bottom_t: str

    cross: str


ROUNDED = BorderStyle(
    top_left="╭",
    top_right="╮",
    bottom_left="╰",
    bottom_right="╯",
    horizontal="─",
    vertical="│",
    left_t="├",
    right_t="┤",
    top_t="┬",
    bottom_t="┴",
    cross="┼",
)

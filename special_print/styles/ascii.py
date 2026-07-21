"""
ASCII border style.
"""

from .rounded import BorderStyle

ASCII = BorderStyle(
    top_left="+",
    top_right="+",
    bottom_left="+",
    bottom_right="+",
    horizontal="-",
    vertical="|",
    left_t="+",
    right_t="+",
    top_t="+",
    bottom_t="+",
    cross="+",
)

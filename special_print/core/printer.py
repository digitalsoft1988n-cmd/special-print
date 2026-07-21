"""
Printing utilities for Special Print.
"""

from __future__ import annotations

from typing import Any, TextIO
import sys


class Printer:
    """Handles output of rendered content."""

    def __init__(self, stream: TextIO | None = None):
        self.stream = stream or sys.stdout

    def print(
        self,
        content: str,
        *,
        end: str = "\n",
        flush: bool = False,
    ) -> None:
        """
        Print rendered content.

        Parameters
        ----------
        content:
            The rendered string.
        end:
            String appended after the output.
        flush:
            Whether to flush the stream.
        """
        print(
            content,
            file=self.stream,
            end=end,
            flush=flush,
        )


_default_printer = Printer()


def print_rendered(
    content: str,
    *,
    end: str = "\n",
    flush: bool = False,
) -> None:
    """
    Print rendered content using the default printer.
    """
    _default_printer.print(
        content,
        end=end,
        flush=flush,
    )

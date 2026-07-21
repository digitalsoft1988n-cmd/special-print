"""
Base renderer for Special Print.

All renderers should inherit from this class and implement the
`render()` method.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Renderer(ABC):
    """Abstract base class for all renderers."""

    @abstractmethod
    def render(self, value: Any, **kwargs) -> str:
        """
        Convert a Python object into a formatted string.

        Parameters
        ----------
        value:
            The object to render.

        Returns
        -------
        str
            The rendered string.
        """
        raise NotImplementedError

    def print(self, value: Any, **kwargs) -> None:
        """
        Render and print the value.
        """
        print(self.render(value, **kwargs))

#!/usr/bin/env python3
"""A function that returns a multiplier function, with type annotations."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its float input by multiplier."""

    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func

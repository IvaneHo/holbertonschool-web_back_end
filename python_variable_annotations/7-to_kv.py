#!/usr/bin/env python3
"""A function that returns a tuple (string, square of int/float as float), with type annotations."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and the square of v as a float."""
    return (k, float(v**2))

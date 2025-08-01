#!/usr/bin/env python3
"""A function that returns the sum of a list of floats, with type annotations."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floats in input_list."""
    return sum(input_list)

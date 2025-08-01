#!/usr/bin/env python3
"""A function that returns the sum of a mixed list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all ints and floats in mxd_lst as a float."""
    return sum(mxd_lst)

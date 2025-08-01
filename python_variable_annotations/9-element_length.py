#!/usr/bin/env python3
"""A function that returns a list of tuples (item, length), with type annotations."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples (element, length of element) for each item in lst."""
    return [(i, len(i)) for i in lst]

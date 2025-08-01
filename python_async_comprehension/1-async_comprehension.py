#!/usr/bin/env python3
"""
A module that defines an asynchronous comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers and returns them

    Returns:
    10 random numbers
    """
    numbers = [num async for num in async_generator()]
    return numbers

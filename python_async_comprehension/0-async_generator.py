#!/usr/bin/env python3
"""
This module provides a method
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The said method
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

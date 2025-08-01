#!/usr/bin/env python3
"""
This module provides an async coroutine that wait and return a random delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    The said method
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

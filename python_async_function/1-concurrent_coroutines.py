#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay and return sorted list of all delays."""
    delays = []
    for coroutine in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await coroutine
        delays.append(delay)
    return delays

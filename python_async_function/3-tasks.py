#!/usr/bin/env python3
"""
This module contains a method
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    The said method
    """
    return asyncio.create_task(wait_random(max_delay))

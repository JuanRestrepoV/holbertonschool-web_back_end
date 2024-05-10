#!/usr/bin/env python3
"""
measure_runtime should
measure the total runtime
and return it.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime should
    measure the total runtime
    and return it.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    return time.time() - start_time

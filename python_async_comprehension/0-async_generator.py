#!/usr/bin/env python3
"""
coroutine will loop 10 times,
Seach time asynchronously
wait 1 second, then yield
Sa random number between 0
Sand 10. Use the random module.
"""
import asyncio
import random


async def async_generator():
    """
    No arguments
    """
    for _ in range (0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

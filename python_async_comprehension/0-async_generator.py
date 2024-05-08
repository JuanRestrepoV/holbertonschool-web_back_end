#!/usr/bin/env python3
"""
coroutine will loop 10 times,
Seach time asynchronously
wait 1 second, then yield
Sa random number between 0
Sand 10. Use the random module.
"""
import asyncio
from random import uniform
from typing import AsyncIterator, AsyncGenerator


async def async_generator() -> AsyncIterator[ AsyncGenerator[int, None] ]:
    """
    No arguments
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

#!/usr/bin/env python3
"""
return the list of all
the delays (float values).
The list of the delays should
be in ascending order without
using sort() because of
concurrency.
"""
import asyncio
from typing import List
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    sorted_list = []
    for _ in range(n):
        sorted_list.append(wait_random(max_delay))
    sorted_list = await asyncio.gather(*sorted_list)
    return sorted(sorted_list)

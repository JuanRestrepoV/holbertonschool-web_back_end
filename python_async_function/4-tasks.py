#!/usr/bin/env python3
"""
Take the code from wait_n and
alter it into a new function
task_wait_n. The code is nearly
identical to wait_n except
task_wait_random is being called.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    sorted_list = []
    for _ in range(n):
        sorted_list.append(task_wait_random(max_delay))
    sorted_list = await asyncio.gather(*sorted_list)
    return sorted(sorted_list)

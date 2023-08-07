#!/usr/bin/env python3

"""Asynchronous functions"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ A function that that takes an integer max_delay and n,
        returns a list of delays """
    delay_list: List[float] = []
    for i in range(n):
        delay = await task_wait_random(max_delay)
        delay_list.append(delay)
    return delay

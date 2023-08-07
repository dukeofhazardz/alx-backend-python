#!/usr/bin/env python3

"""Asynchronous functions"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ A function that return the list of all the delays (float values)
        in ascending order without using sort() because of concurrency. """
    delay_list: List[float] = []

    delays: dict = {i: task_wait_random(max_delay) for i in range(n)}
    await asyncio.gather(*delays.values())
    delay_list = [delay.result() for delay in sorted(delays.values(),
                                               key=lambda x: x.result())]

    return delay_list

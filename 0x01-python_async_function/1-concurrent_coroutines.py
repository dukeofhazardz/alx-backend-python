#!/usr/bin/env python3

"""Asynchronous functions"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ A function that return the list of all the delays (float values)
        in ascending order without using sort() because of concurrency. """
    delay_list: List[float] = []

    delays: dict = {i: await wait_random(max_delay) for i in range(n)}
    delay_list = [delay for _, delay in sorted(delays.items(),
                                               key=lambda x: x[1])]

    return delay_list

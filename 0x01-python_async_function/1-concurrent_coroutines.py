#!/usr/bin/env python3

"""Asynchronous functions"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ A function that  return the list of all the delays (float values)
        in ascending order without using sort() because of concurrency. """
    delay_list: list[float] = []

    for i in range(n):
        delay: float = await wait_random(max_delay)
        delay_list.append(delay)
    delay_list.sort()
    return delay_list

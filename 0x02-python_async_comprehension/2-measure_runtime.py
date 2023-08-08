#!/usr/bin/env python3

"""Async Comprehension"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ A coroutine that will execute async_comprehension four times in
        parallel using asyncio.gather, measure the total runtime and
        return it. """
    startTime: float = time.perf_counter()
    coroutine = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coroutine)
    endTime: float = time.perf_counter()
    totalTime: float = endTime - startTime
    return totalTime

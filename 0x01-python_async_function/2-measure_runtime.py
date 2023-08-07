#!/usr/bin/env python3

"""Asynchronous functions"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ A function that measures the total execution time for
        wait_n(n, max_delay), and returns total_time / n """
    startTime: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    endTime: float = time.perf_counter()
    totalTime: float = endTime - startTime
    return totalTime / n

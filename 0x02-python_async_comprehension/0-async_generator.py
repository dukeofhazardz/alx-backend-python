#!/usr/bin/env python3

"""Async Comprehension"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ A coroutine will loop 10 times, each time asynchronously wait
        1 second, then yield a random number between 0 and 10. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

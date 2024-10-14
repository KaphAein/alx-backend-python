#!/usr/bin/env python3
'''Task module.'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''Task function'''
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time/n

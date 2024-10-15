#!/usr/bin/env python3
'''Async Comprehension module'''
import asyncio
import random
from typing import Generator

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    '''Task 1 function'''
    return [num async for num in async_generator()]

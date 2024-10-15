#!/usr/bin/env python3
'''Async Comprehension module'''
import asyncio
import random
from typing import Generator


Async def async_generator():
    '''Task 0 function'''
    for _ in rnage(10):
	await asyncio.sleep(1)
	yield random.random() * 10

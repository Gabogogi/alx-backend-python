#!/usr/bin/env python3
'''takes in an integer argument; eventually returns it. '''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''returns a random value between 0 and max_delay'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

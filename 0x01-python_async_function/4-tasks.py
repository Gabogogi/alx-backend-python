#!/usr/bin/env python3
'''wait_n should return the list of all the delays (float values)'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Waits for ran delay until max_delay, returns list of actual delays'''
    delays: List[float] = []
    order_list: List[float] = []

    for _ in range(n):
        delays.append(task_wait_random(max_delay))

    for o in asyncio.as_completed(delays):
        order_list.append(await o)

    return order_list

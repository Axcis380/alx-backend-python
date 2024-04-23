#!/usr/bin/env python3
'''Task 1 mod.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creat list of 10 num from 10num generat.
    '''
    return [num async for num in async_generator()]

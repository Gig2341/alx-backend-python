#!/usr/bin/env python3

'''
this module imports async_generator from the previous task and then write a
coroutine called async_comprehension that takes no arguments. The coroutine 
collects 10 random numbers using an async comprehensing over async_generator,
then return the 10 random numbers.
'''


import asyncio
import random
async_generator = ('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    

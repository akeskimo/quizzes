#!/usr/bin/env python3

import pytest
import random
from concurrent.futures import ThreadPoolExecutor
import asyncio
from packages.binarytrees.binarytrees import solution
from .testlib import BoundedArray


@pytest.mark.parametrize("args,expected", (
    (([1,2,3,4], 1), 0),
    (([1,2,3,4], 2), 1),
    (([1,2,3,4], 3), 2),
    (([1,2,3,4], 4), 3),
    (([1,2,3,4,5,6,7,8,9,10,11,12,14], 7), 6),
    (([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 14), 13),
    (([1,2,3,4], 5), -1),
    (([1,2,3,4], 0), -1),
    (([1,3], 1), 0),
    (([1,3], 3), 1),
    (([-1,0], 0), 1),
    (([-10, -2], -10), 0),
    (([1], 1), 0),
    (([], 1), -1),
))
def test_simple_cases(args, expected):
    assert expected == solution(*args)


@pytest.mark.parametrize("args,expected", (
    (([], 1), -1),
    (([], -1000), -1),
    (([-200, 200], -200), 0),
    (([-200, 200], 200), 1),
    (([-200, 200], 201), -1),    
))
def test_edge_cases(args, expected):
    assert expected == solution(*args)


@pytest.mark.parametrize("size,iterations", (
    ([0, 10], 1),
    ([0, 100], 100),
    ([-100, 0], 100),
    ([-2000000, 0], 1),
    ([-2000000, 2000000], 10),
    ([-20000000, 20000000], 1),
))
def test_uniform_large_array_with_timeout(size, iterations):
    waiting_for_result_timeout_seconds = 5

    def create_uniform_array(size):
        arr = BoundedArray(*size)
        value = random.randint(size[0], size[1]-1)
        idx = arr.index(value)
        return arr, value, idx

    async def block_until_task_finished():
        A, R, expected = create_uniform_array(size)
        f = loop.run_in_executor(None, solution, A, R)
        assert expected == await asyncio.wait_for(f, timeout=waiting_for_result_timeout_seconds)

    loop = asyncio.get_event_loop()
    futures = [block_until_task_finished() for _ in range(iterations)]
    loop.run_until_complete(asyncio.gather(*futures))

#!/usr/bin/env python3


"""
Description:
Given data array A and value R derive a solution algorithm
that returns the index of R in A. If value does not exist,
the function should return value -1.


Data description:
- The values in array A are sorted in increasing order.
- Array values are in range [-20000000, 20000000].
- Array size is in range [0, 4000000].
- Searched value is in range [-20000000, 20000000].
"""

import argparse
import sys
import pytest
import logging
import random
from concurrent.futures import ThreadPoolExecutor, as_completed


def solution(A, R):
    len_A = len(A)
    l = 0
    r = len_A
    while l < r:
        m = (l + r) // 2
        if A[m] < R:
            l = m
            r -= 1
        else:
            r = m
        if A[r] == R:
            return r
    return -1


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
    ([0, 100], 100),
    ([-100, 0], 100),
    ([-2000000, 0], 1),
    ([-2000000, 2000000], 1),
))
def test_uniform_large_array_with_timeout(size, iterations):
    waiting_for_result_timeout_seconds = 1

    def create_uniform_array(size):
        arr = [x for x in range(*size)]
        value = random.choice(arr)
        idx = arr.index(value)
        return arr, value, idx

    with ThreadPoolExecutor() as executor:
        A, R, expected = create_uniform_array(size)
        futures = {executor.submit(solution, A, R) for _ in range(iterations)}
        for f in futures:
            assert expected == f.result(timeout=waiting_for_result_timeout_seconds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Binary tree search.")
    parser.add_argument("A", help="Data array as list separated by commas, e.g. 1,2,3,4,5,6.")
    parser.add_argument("R", type=int, help="Search value, e.g. 3.")
    args = parser.parse_args(sys.argv[1:])
    
    # convert string to list of integers
    try:
        args.A = [int(a) for a in args.A.split(",")]
    except ValueError as e:
        print(f"invalid value: {e}")
        sys.exit(1)

    print(solution(args.A, args.R))
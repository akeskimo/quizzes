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


def solution(A, R):
    left = 0
    right = len(A)
    while left < right:
        middle = (left + right) // 2
        if A[middle] < R:
            left = middle
            right -= 1
        else:
            right = middle
        if A[right] == R:
            return right
    return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Binary tree search.")
    parser.add_argument(
        "A", help="Data array as list separated by commas, e.g. 1,2,3,4,5,6."
    )
    parser.add_argument("R", type=int, help="Search value, e.g. 3.")
    args = parser.parse_args(sys.argv[1:])

    # convert string to list of integers
    try:
        args.A = [int(a) for a in args.A.split(",")]
    except ValueError as e:
        print(f"invalid value: {e}")
        sys.exit(1)

    print(solution(args.A, args.R))

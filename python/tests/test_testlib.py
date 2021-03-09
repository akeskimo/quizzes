#!/usr/bin/env python3

import pytest
from .testlib import BoundedArray


def assert_index_out_of_range(arr, index):
    with pytest.raises(IndexError):
        arr[index]


def test_bounded_array_getitem():
    size = (0, 10)
    arr = BoundedArray(*size)
    for value in [value for value in range(*size)]:
        assert arr[value] == value

    assert_index_out_of_range(arr, size[1] + 1)
    assert_index_out_of_range(arr, -size[1] - 1)


@pytest.mark.parametrize("size,expected", (
    ((0,1), 1),
    ((0,100), 100),
    ((21,2939), 2918),
))
def test_len(size, expected):
    arr = BoundedArray(*size)
    assert expected == len(arr)


def test_index():
    size = (3,5)
    arr = BoundedArray(*size)
    assert arr.index(3) == 0
    assert arr.index(4) == 1

    with pytest.raises(ValueError):
        arr.index(size[0]-1)

    size = (66,12345)
    arr = BoundedArray(*size)
    assert arr.index(size[1]) == size[1] - size[0]
    import random
    for _ in range(100):
        random_value = random.randint(*size)
        assert random_value - size[0] == arr.index(random_value)


def test_for_loop():
    size = (0, 10)
    arr = BoundedArray(*size)
    ref = [l for l in range(*size)]

    for expected, actual in zip(ref, arr):
        assert expected == actual

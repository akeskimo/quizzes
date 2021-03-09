#!/usr/bin/env python3

from collections.abc import MutableSequence


class BoundedArray(MutableSequence):
    """
    Low-memory data structure for testing algorithms that
    require large data sets.

    Usage:
      arr = BoundedArray(22, 100)
      for value in arr:
          print(value)
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._len = self.end - self.start

    def __getitem__(self, index):
        index = index if index >= 0 else -index
        if index > self._len:
            raise IndexError(f"index {index} out of range")
        return self.start + index

    def __len__(self):
        return self.end - self.start

    def __delitem__(self, index):
        raise NotImplemented

    def __setitem__(self, index, value):
        raise NotImplemented

    def insert(self, index, value):
        raise NotImplemented

    def __str__(self):
        return f"<BoundedArray([{self.start},{self.end}]) {id(self)}>"

    def __repr__(self):
        return self.__str__()

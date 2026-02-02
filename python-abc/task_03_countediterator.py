#!/usr/bin/python3
"""CountedIterator: tracks iterator calls"""


class CountedIterator:
    """Iterator wrapper with call counter"""

    def __init__(self, iterable):
        """Initialize iterator and counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Increment count and yield next item"""
        self.count += 1
        next_item = next(self.iterator)
        return next_item

    def get_count(self):
        """Return iteration count"""
        return self.count

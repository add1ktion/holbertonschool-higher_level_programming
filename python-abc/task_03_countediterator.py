#!/usr/bin/python3
"""CountedIterator module."""


class CountedIterator:
    """Iterator that tracks iteration count."""

    def __init__(self, iterable):
        """Initialize iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Get next item and increment count."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            self.count += 1
            raise

    def get_count(self):
        """Return number of items iterated."""
        return self.count

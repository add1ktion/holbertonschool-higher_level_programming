#!/usr/bin/python3
"""
Prints a square of size x size with # character.
Prototype: def print_square(size):
- size must be integer >= 0
- Raises TypeError if not int, ValueError if < 0
- size=0 prints nothing.
"""


def print_square(size):
    """
    Prints square of given size.

    Args:
        size (int): Square side length >= 0

    Raises:
        TypeError: If size not integer
        ValueError: If size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

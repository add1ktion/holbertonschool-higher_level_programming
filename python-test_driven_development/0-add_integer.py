#!/usr/bin/python3
"""Adds 2 integers.

Prototype: def add_integer(a, b=98):
- a and b must be integers or floats, otherwise raise a TypeError
  exception with the message `a must be an integer` or `b must be an integer`
- a and b must be first casted to integers (if they are floats)
- Returns an integer: the addition of a and b
- You are not allowed to import any module
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): First number.
        b (int, float): Second number (default 98).

    Returns:
        int: Sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(float(a))
    b = int(float(b))
    return int(a) + int(b)

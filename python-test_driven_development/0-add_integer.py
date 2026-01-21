#!/usr/bin/python3
"""Adds 2 integers. a and b must be integers or floats,
otherwise raise a TypeError exception.
a and b must be first casted to integers (if float) and return int sum."""


def add_integer(a, b=98):
    """
    Adds 2 integers.
    Args: a (int, float): first number. b (int, float): second number.
    Return: int: Sum of a + b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

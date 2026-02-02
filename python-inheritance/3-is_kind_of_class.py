#!/usr/bin/python3
"""Module with method is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Return True if an object is an
    instance of a class that inherited"""

    return isinstance(obj, a_class)

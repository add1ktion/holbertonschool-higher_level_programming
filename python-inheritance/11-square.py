#!/usr/bin/python3
"""Module with class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Init Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Square description"""
        return ("[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height)
        )

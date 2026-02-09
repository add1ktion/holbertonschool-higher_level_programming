#!/usr/bin/python3


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict representation with optional attrs filter."""
        if attrs is None:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

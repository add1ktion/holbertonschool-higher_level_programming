#!/usr/bin/python3
"""Geometric shapes with duck typing"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract shape with area and perimeter"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle with radius"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle with width and height"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


def shape_info(shape):
    """Print shape area and perimeter"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

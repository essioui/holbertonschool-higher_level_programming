#!/usr/bin/python3
"""Define class with using library abc"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    shape have two methods area and perimeter \
    inherit from class shape.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """
    circle inherit from shape and calcul radius
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    rectangle inherit from shape define width and height
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    print area and perimeter
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

if __name__ == "__main__":
    # Instantiation a Circle and a Rectangle
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    # Print information of shapes
    shape_info(circle)
    shape_info(rectangle)
#!/usr/bin/python3
"""Define class with using library abc"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Shape abstract class with two methods: area and perimeter.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape and calculating radius.
    """

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape and defining width and height.
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of the shape.
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

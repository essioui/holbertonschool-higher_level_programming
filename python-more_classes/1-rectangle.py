#!/usr/bin/python3
"""
Definie Rectangle class
"""


class Rectangle:
    """
    Represent new rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        new Rectangle
        Args:
        width (int): must be a integer positif
        height (int): must be a integer positif
        """
        self.width = width
        self.height = height

    def width(self):
        return (self.__width)

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return (self.__height)

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value



#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(-2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

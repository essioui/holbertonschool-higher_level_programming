#!/usr/bin/python3
"""
Define Rectangle class
"""


class Rectangle:
    """
    Represent a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize rectangle with width and height
        Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        else:
            return 2 * (self._width + self._height)

    def __str__(self):
        """
        Represent the rectangle by #
        """
        if self._width == 0 or self._height == 0:
            return ("")
        else:
            Rectangle = ('#' * self._width + '\n') * self._height
            return (Rectangle.rstrip('\n'))

#!/usr/bin/python3
"""
This module defines a class Rectangle.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    ...

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle

    Methods:
        width(): Gets the width of the rectangle
        width(value): Sets the width of the rectangle
        height(): Gets the height of the rectangle
        height(value): Sets the height of the rectangle
        area(): return the area of the rectangle
        perimeter(): return the perimeter of the rectangle
        __str__(): Prints the rectangle with the character #
        __repr__(): Returns a string representation to recreate a new instance
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Constructs all attributes for the rectangle object.

        Parameters:
            width (int, optional): Width of the rectangle
            height (int, optional): Height of the rectangle)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:

        value (int): Width of the rectangle

        Raises:

        TypeError: If width is not an integer
        ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters:

        value (int): Height of the rectangle

        Raises

        TypeError: If height is not an integer
        ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

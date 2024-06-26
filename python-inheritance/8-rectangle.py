#!/usr/bin/python3
"""Define class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """Class Rectangle using class BaseGeometry"""

    def __init__(self, width, height):

        """Intialize a new Rectangle.
        Args:
            width (int): The width of Rectangle.
            height (int): The height of  Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""
Definie Rectangle class
"""


class Rectangle:
    """
    Class Rectangle
    Args:
    width (int): must be a integer positif
    height (int): must be a integer positif
    Raises:
    TypeError: width must be an integer
    ValueError: width must be >= 0
    TypeError: height must be an integer
    ValueError: height must be >= 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        return (self.width)
    
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    def height(self):
        return (self.height)
    
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        try:
            my_rectangle = Rectangle(2, -3)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        try:
            my_rectangle = Rectangle(-2, 3)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

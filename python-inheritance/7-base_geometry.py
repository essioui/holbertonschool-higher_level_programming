#!/usr/bin/python3
"""Define class"""


class BaseGeometry:
    """
    based on 6-base_geometry.py
    """

    def area(self):
        """that raises an Exception with the message"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Function validation of integer
        Args:
        name (str): must be an string
        value (int): must be an integer and greater of zero
        Raises:
        TypeError: <name> must be an integer
        ValueError: <name> must be greater than 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater 0")


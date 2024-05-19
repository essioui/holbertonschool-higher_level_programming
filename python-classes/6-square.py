#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
        
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self):
        return self.__position

    def position(self, value):
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
            return None
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

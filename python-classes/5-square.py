#!/usr/bin/python
class Square:
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for _ in range(0, self.__size):
            print("#" * self.__size)
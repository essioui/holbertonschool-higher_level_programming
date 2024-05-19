#!/usr/bin/python3
class Square:
    """Square Class

    A Square Class

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square."""
        self.size = size
        self.position = position

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self):
        return self.__position

    def position(self, value):
        '''Sets position attribute'''
        if len(value) < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        '''Prints stdout square with character #'''
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for blanks in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()

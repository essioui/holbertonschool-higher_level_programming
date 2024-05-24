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
        
    def __repr__(self):
        """
        return a string representation of the rectangle \
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

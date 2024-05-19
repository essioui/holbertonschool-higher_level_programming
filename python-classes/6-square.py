class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value
    
    def my_print(self):
        if self.size == 0:
            print("")
            return
        
        # Print the vertical offset
        for _ in range(self.position[1]):
            print("")
        
        # Print the square rows with the horizontal offset
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)


#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

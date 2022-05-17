#!/usr/bin/python3
"""define class square and prints it with size and coordinates"""


class Square:
    """create square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize public square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size input"""
        return self.__size

    @size.setter
    def size(self, size):
        """define size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """coordinate getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """define position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area size"""
        return self.__size * self.__size

    def my_print(self):
        """prints to stdout square with # symbol"""
        if self.size == 0:
            print()
        else:
            position = self.position
            if position[1] > 0:
                for i in range(position[1]):
                    print()
            for i in range(self.size):
                print(" " * position[0], end="")
                print('#' * self.size)

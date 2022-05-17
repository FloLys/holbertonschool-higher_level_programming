#!/usr/bin/python3
"""define size and area of a square class with getter and setter"""


class Square:
    """create square class"""

    def __init__(self, size=0):
        """initialize public square"""
        self.size = size

    @property
    def size(self):
        """size input"""
        return self.__size

    def area(self):
        """area size"""
        return self.__size * self.__size

    @size.setter
    def size(self, size):
        """define size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """prints to stdout square with # symbol"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)

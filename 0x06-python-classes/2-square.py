#!/usr/bin/python3
"""define size of a square by its input with conditionals"""


class Square:
    """create square class"""
    def __init__(self, size=0):
        """define private size with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

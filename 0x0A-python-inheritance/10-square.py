#!/usr/bin/python3
""" Rectangle module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Subclass """

    def __init__(self, size):
        """ instantiation """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area = width * height """
        return (self.__size * self.__size)

    def __str__(self):
        """ rectangle description """
        return (f"[Rectangle] {self.__size}/{self.__size}")

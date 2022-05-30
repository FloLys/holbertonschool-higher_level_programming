#!/usr/bin/python3
""" Rectangle module """


class BaseGeometry():
    """ Class """

    def area(self):
        """raises an Exception message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value, name is always a string """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Subclass """

    def __init__(self, width, height):
        """ instantiation """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

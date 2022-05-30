#!/usr/bin/python3
""" Integer validator """


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

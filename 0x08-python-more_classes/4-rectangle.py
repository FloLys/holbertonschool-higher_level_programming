#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """initialize rectangle"""
        self.height = height
        self.width = width

    def __repr__(self):
        """representation of rectangle to recreate"""
        return (f"{self.__class__.__name__}({self.width}, {self.height})")

    def __str__(self):
        """print rectangle with # """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (f"{'#'*self.width}\n"*self.height).strip('\n')

    def area(self):
        """area: width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter: (width*2) + (height*2)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width*2 + self.__height*2

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

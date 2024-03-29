#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize data"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        """Representation of rectangle to instance copy"""
        return (f"{self.__class__.__name__}({self.width}, {self.height})")

    def __str__(self):
        """Print rectangle with symbol"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (f"{self.print_symbol*self.width}\n"*self.height)\
                         .strip('\n')

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

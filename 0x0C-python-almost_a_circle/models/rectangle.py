#!/usr/bin/python3
""" Module first rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializator """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Area = width * height """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle with # """
        print('\n' * self.__y, end="")
#        for i in range(self.__height):
#            print(' ' * self.__x, end="")
#            print('#' * self.__width)
        print(f"{(' '*self.__x)}{'#'*self.__width}\n" * self.__height, end="")

    def __str__(self):
        """ Print string method """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ Updates arguments """
        attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
# setattr creates or references the attr with the name string given
# object.name = self."id" = self.id
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Returns the dict representation of the Rectangle """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ X Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ X Setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Y Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y Setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

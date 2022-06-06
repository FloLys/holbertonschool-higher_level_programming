#!/usr/bin/python3
""" Module Square """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializator """

        super().__init__(size, size, x, y, id)

    def area(self):
        """ Area = size * size """
        return self.size * self.size

    def display(self):
        """ Prints the square with # """
        print('\n' * self.y, end="")
#        for i in range(self.__height):
#            print(' ' * self.__x, end="")
#            print('#' * self.__width)
        print(f"{(' ' * self.x)}{'#' * self.size}\n" * self.size, end="")

    def __str__(self):
        """ Print string method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """ Updates arguments """
        attr = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
# setattr creates or references the attr with the name string given
# object.name = self."id" = self.id
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Returns the dict representation of Square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        """ Size Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size Setter """
        self.width = value
        self.height = value

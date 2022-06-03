#!/usr/bin/python3
""" Models """


class Base():
    """ Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initiator """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

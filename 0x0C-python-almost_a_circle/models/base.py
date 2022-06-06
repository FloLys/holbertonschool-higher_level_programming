#!/usr/bin/python3
""" Models """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation of list_dictionaries """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the str of list_objs to a file """
        if list_objs is None:
            list_objs = []
        list_objs = cls.to_json_string([attr.to_dictionary()
                                        for attr in list_objs])
        with open(cls.__name__+'.json', 'w') as f:
            f.write(list_objs)

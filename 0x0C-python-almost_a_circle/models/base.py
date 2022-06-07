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

    @staticmethod
    def from_json_string(json_string):
        """ List of JSON string representation """
        if json_string is None or not json_string:
            return json_string
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the str of list_objs to a file """
        if list_objs is None:
            list_objs = []
        list_objs = cls.to_json_string([attr.to_dictionary()
                                        for attr in list_objs])
        with open(cls.__name__+'.json', 'w') as f:
            f.write(list_objs)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attr set """
        if cls.__name__ == 'Rectangle':
            copy_cls = cls(1, 1)
        if cls.__name__ == 'Square':
            copy_cls = cls(1)
        copy_cls.update(**dictionary)
        return copy_cls

    @classmethod
    def load_from_file(cls):
        """ Returns a list """
        if cls is None:
            return '[]'
        with open(cls.__name__+'.json', 'r') as f:
            listinfo = cls.from_json_string(f.read())
        return [cls.create(**dic) for dic in listinfo]

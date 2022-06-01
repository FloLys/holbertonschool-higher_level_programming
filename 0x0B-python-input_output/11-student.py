#!/usr/bin/python3
""" Student to JSON """


class Student():
    """ Class """

    def __init__(self, first_name, last_name, age):
        """ Instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dict description with simple data structure """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for elem in attrs:
                if elem in self.__dict__.keys() and isinstance(elem, str):
                    dic[elem] = self.__dict__[elem]
            return dic

    def reload_from_json(self, json):
        """ Replaces all attr from Json to Student """
        for key, value in json.items():
            setattr(self, key, value)

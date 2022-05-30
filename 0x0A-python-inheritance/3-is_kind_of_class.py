#!/usr/bin/python3
""" Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """ Returns True if the obj is an instance of the
    specified class or inherited from, otherwise False """

    return isinstance(obj, a_class)

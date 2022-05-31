#!/usr/bin/python3
""" Add Attribute """


def add_attribute(obj, name, value):
    """ Adds a new attribute to an objects if possible """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)

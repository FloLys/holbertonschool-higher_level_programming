#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """ returns the dict description with simple data structure for json obj"""
    return obj.__dict__

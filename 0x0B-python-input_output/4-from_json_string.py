#!/usr/bin/python3
import json
""" From JSON string to object """


def from_json_string(my_str):
    """ Returns an object represented by JSON string """
    return json.loads(my_str)

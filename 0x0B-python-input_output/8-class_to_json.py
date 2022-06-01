#!/usr/bin/python3
""" Class to JSON """
import json


def class_to_json(obj):
    """ returns the dict description with simple data structure for json obj"""

    json_string = json.dumps(obj.__dict__)
    return json.loads(json_string)

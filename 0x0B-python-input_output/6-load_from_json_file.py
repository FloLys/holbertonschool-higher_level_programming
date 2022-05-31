#!/usr/bin/python3
""" Create object from json file """
import json


def load_from_json_file(filename):
    """ Creates an object from a json filen """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

#!/usr/bin/python3
""" Write File """


def write_file(filename="", text=""):
    """ Writes a string to a text file in utf8 and returns count of chars """
    if not filename:
        filename = ""

    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))

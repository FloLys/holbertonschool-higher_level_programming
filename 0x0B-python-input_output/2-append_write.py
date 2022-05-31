#!/usr/bin/python3
""" Append to File """


def append_write(filename="", text=""):
    """ Appends a string at the end and returns count of chars """

    if not filename:
        filename = ""

    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))

#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ Reads a text file in UTF8 and prints to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

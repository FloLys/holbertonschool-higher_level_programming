#!/usr/bin/python3
""" My list """


class MyList(list):
    """ class """

    def print_sorted(self):
        """ prints a sorted list """
        return print(sorted(self))

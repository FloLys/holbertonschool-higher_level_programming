#!/usr/bin/python3
""" My integer """


class MyInt(int):
    """ Class of integers """

    def __eq__(self, other):
        """ Returns True a comparison == between a and b if equals"""
        return (self is other)

    def __ne__(self, other):
        """ Negates equals """
        return not (self is other)

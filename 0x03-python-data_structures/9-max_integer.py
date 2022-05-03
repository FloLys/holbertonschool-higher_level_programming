#!/usr/bin/python3
def max_integer(my_list=[]):
    maxint = 0
    for i in my_list:
        if i > maxint:
            maxint = i
    return maxint

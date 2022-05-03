#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    element = [0, 0]
    for i, elem in enumerate(tuple_a):
        if not elem:
            continue
        element[i] += tuple_a[i]
    for i, elem in enumerate(tuple_b):
        if not elem:
            continue
        element[i] += tuple_b[i]
    new_tuple = (element[0], element[1])
    return new_tuple

#!/usr/bin/python3
def no_c(my_string):
	dest_string = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        dest_string += char
    return dest_string

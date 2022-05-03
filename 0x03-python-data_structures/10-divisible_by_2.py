#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    i = 0
    if my_list:
        for elem in my_list:
            if elem % 2 == 0:
                new_list[i] = True
            else:
                new_list[i] = False
            i += 1
        return new_list

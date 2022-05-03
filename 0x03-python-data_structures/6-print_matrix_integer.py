#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        array_len = len(x)
        for y in range(array_len):
            print("{}{}".format(x[y], ' ' if y != array_len - 1 else ''),
                  end='')
        print()

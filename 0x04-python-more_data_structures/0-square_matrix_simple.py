#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i, x in enumerate(matrix):
        new_matrix.append(list(map(lambda x: x * x, matrix[i])))
#        new_matrix[i] = x.copy()
#        for j, y in enumerate(x):
#            new_matrix[j] = y^2
    return new_matrix

#!/usr/bin/python3
""" Divide all elements of a matrix """


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix """

    newmatrix = []

    if matrix == None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        return matrix

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for array in matrix:
        if not isinstance(array, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(array) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for element in array:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        newmatrix.append(list(map(lambda x: round(x/div, 2), array)))

    return newmatrix

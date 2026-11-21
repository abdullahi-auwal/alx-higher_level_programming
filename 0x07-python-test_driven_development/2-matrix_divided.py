#!/usr/bin/python3
"""This module contains modules that divide a matrix"""


def matrix_divided(matrix, div):
    """
    Perform division on a matrix.

    Args:
        matrix (list): a matrix of ints or floats
        div (int, float): divides the elements of the matrix

    Return:
        list: list containing results of each element division
    """
    new_matrix = []

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats"
                        )

    col1 = len(matrix[0])
    for i in matrix:
        col2 = len(i)
        if col2 != col1:
            raise TypeError("Each row of the matrix must have the same size")
        in_matrix = []
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats"
                                )
            result = round(j / div, 2)
            in_matrix.append(result)
        new_matrix.append(in_matrix)

    return new_matrix

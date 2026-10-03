#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    if len(matrix) == 0:
        return matrix
    for j in matrix:
        a.append(list(map(lambda x: x*x, j)))
    return a

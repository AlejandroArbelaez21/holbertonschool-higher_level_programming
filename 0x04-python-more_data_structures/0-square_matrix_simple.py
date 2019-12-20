#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list = matrix.copy()
    return [[x*x for x in row] for row in list]

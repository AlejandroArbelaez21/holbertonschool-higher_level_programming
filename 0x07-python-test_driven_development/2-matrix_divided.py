#!/usr/bin/python3
def matrix_divided(matrix, div):
    other = []
    text = "matrix must be a matrix (list of lists) of integers/floats"
    text2 = "Each row of the matrix must have the same size"
    size = len(matrix[0])
    if (matrix):
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if type(matrix) is not list:
            raise TypeError(text)
        for y in range(len(matrix)):
            if type(matrix[y]) is not list:
                raise TypeError(text)
        for x in matrix:
            if size != len(x):
                raise TypeError(text2)
        for row in matrix:
            for elem in row:
                if type(elem) is not int and type(elem) is not float:
                    raise TypeError(text)
        for row in matrix:
            new = []
            for elem in row:
                new.append(round(elem / div, 2))
            other.append(new)
    return(other)

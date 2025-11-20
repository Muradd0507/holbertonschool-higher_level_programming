#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s = []
    for i in matrix:
        result = list(map(lambda x: x**2, i))
        s.append(result)
    return s

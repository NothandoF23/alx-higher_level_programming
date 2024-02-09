#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new = matrix.copy()
        size = len(matrix)
        for i in range(0, size):
            new[i] = list(map(lambda n: n*n, matrix[i]))
        return (new)

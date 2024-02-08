#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for idx in i:
                if idx != i[-1]:
                    print("{:d}".format(idx), end=" ")
                else:
                    print("{:d}".format(idx), end="")
            print()

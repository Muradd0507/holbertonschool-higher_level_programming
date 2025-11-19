#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = 0
        for j in i:
            if (j == i[-1]):
                print("{:d}".format(j), end=' ')
            else:
                print("{:d}".format(j), end=' ')
        if (k == len(matrix)):
            pass
        else:
            print("\n")
        k += 1

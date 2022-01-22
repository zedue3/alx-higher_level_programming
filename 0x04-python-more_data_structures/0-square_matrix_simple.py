#!/usr/bin/python3
def square(x):
    return x * x

def square_matrix_simple(matrix=[]):

    new_matrix = matrix[:]

    for i in range(len(new_matrix)):
        new_matrix[i] = map(square, new_matrix[i])

    return new_matrix

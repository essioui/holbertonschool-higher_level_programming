#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        square_row = []
        for j in i:
            square_row.append(j ** 2)
        square_matrix.append(square_row)
    return (square_matrix)

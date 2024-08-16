#!/usr/bin/python3
"""
 0x07. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates 2D matrix using in place operation
        first transpose the matrixe then reverse each row.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in range(n):
        matrix[row].reverse()

    return matrix

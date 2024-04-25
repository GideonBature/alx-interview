#!/usr/bin/python3
"""0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it
    90 degrees clockwise

    @Args:
        matrix (nested list): The 2D Matrix

    @Returns:
        matrix (nested list): The rotated 2D Matrix
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

#!/usr/bin/python3
"""0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Pascal's triangle of n

    param: n (int)
    returns: list of lists
    """
    triangle = []

    for i in range(n):
        row = [1]

        for j in range(1, i):
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)

        if i != 0:
            row.append(1)

        triangle.append(row)

    return triangle

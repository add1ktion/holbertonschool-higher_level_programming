#!/usr/bin/python3
"""Returns Pascal's triangle of n."""


def pascal_triangle(n):
    """Returns Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[-1]
        next_row = [1]

        for j in range(len(previous_row) - 1):
            next_row.append(previous_row[j] + previous_row[j + 1])

        next_row.append(1)
        triangle.append(next_row)

    return triangle

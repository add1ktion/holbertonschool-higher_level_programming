#!/usr/bin/python3
"""
Divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
- matrix must be a matrix (list of lists) of integers/floats
- Each row of the matrix must have the same size
- div must be a number
- div can't be equal to 0
- Returns a new matrix
You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): Matrix to divide.
        div (int, float): Divisor.

    Returns:
        list: New matrix with elements divided by div, rounded to 2 decimals.
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    msg3 = "div must be a number"

    if not isinstance(div, (int, float)):
        raise TypeError(msg3)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or len(matrix) == 0 or
       not all(isinstance(row, list) and len(row) > 0 for row in matrix)):
        raise TypeError(msg1)

    first_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_len:
            raise TypeError(msg2)
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg1)

    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]
    return new_matrix

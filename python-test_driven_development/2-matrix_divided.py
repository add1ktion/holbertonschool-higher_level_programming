#!/usr/bin/python3
"""
Divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
- matrix must be list of lists of ints/floats, same size rows
- div must be number (int/float), cannot be 0
- Returns new matrix with elements / div rounded to 2 decimals
- Raises TypeError/ZeroDivisionError on invalid input
"""


def matrix_divided(matrix, div):
    """
    Divides matrix elements by div, returns new matrix rounded to 2dp.

    Args:
        matrix (list): List of lists of numbers
        div (int, float): Divisor (non-zero)

    Returns:
        list: New divided matrix
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    msg3 = "div must be a number"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg1)
    if not isinstance(matrix[0], list):
        raise TypeError(msg1)

    first_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) != first_len:
            raise TypeError(msg2)
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg1)

    if not isinstance(div, (int, float)):
        raise TypeError(msg3)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]
    return new_matrix

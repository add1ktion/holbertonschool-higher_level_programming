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

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"
    msg_div_num = "div must be a number"
    msg_div_zero = "division by zero"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg_type)

    if not isinstance(div, (int, float)):
        raise TypeError(msg_div_num)
    if div == 0:
        raise ZeroDivisionError(msg_div_zero)

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) == 0:
            raise TypeError(msg_type)
        if len(row) != row_size:
            raise TypeError(msg_size)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_type)

    return [[round(element / div, 2) for element in row] for row in matrix]

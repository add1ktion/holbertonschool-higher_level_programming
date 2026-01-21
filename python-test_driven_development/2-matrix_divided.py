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

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError
            ("matrix must be a matrix (list of lists) of integers/floats")
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")

    first_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_len:
            raise TypeError
            ("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        tmp = []
        for el in row:
            tmp.append(round(el / div, 2))
        new_matrix.append(tmp)
    return new_matrix

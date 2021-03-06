#!/usr/bin/python3
"""Divide a matrix
This module contains one function that divide a matrix.
    """


def matrix_divided(matrix, div):
    """ Method that divides a matrix by a integer """

    msj_error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list or not matrix:
        raise TypeError(msj_error)

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not row or type(row) != list:
            raise TypeError(msj_error)

        if len(matrix[0]) is not len(row):
            raise TypeError("Each row of the matrix must have the same size")

        item = []
        for j in row:
            if type(j) is not int and type(j) != float:
                raise TypeError(msj_error)

            numero = round(j / div, 2)
            item.append(numero)
        new_matrix.append(item)

    return new_matrix

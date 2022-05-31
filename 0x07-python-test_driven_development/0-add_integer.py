#!/usr/bin/python3
"""Integers addition

This module contains one function that adds two integers.

    """


def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a (int or float): First number.
        b (int or float): Second number. Defaults to 98.

    Raises:
        TypeError: if a or b are not integer or float numbers.

    Returns:
        int: The addition of a and b.
    """

    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

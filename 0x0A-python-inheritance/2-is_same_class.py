#!/usr/bin/python3

"""Module to check if an object is exactly a class."""


def is_same_class(obj, a_class):
    """ Return if an object is instance of a class """
    if type(obj) is not a_class:
        return False
    return True

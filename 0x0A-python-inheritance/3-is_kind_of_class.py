#!/usr/bin/python3
""" Function to check if an object is an instance of a class
    of an instance of an inherited class"""


def is_kind_of_class(obj, a_class):
    """ Return if an object is instance of a class """
    if isinstance(obj, a_class):
        return True
    return False

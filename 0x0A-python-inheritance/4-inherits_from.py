#!/usr/bin/python3

""" function to check if an object is an instance of a class
    of an instance of an inherited class. """


def inherits_from(obj, a_class):
    """ Return if an object is instance of a class """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)

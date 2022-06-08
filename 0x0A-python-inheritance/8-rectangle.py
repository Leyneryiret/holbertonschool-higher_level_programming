#!/usr/bin/python3

""" Module for geometry class."""


class BaseGeometry:
    """ class BaseGeometry (based on 6-base_geometry.py). """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class Rectangle that
    inherits from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width= width
        super().integer_validator("height", height)
        self.__height = height

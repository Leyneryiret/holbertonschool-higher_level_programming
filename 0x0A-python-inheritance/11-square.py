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
        """ Builder of the Rectangle class """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        return (self.__width * self.__height)


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""

    def __init__(self, size):
        """ Builder of the square class """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))

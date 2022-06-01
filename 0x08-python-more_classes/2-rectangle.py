#!/usr/bin/python3
""" Rectangle
Define the class Rectangle
    """


class Rectangle:
    """ Class rectangle that defines a
    rectangle by: (based on 1-rectangle.py)"""
    
    def __init__(self, width=0, height=0):
        """ Initialize the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that returns the width of the retangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method that sets the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the height of the retangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method that sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method, that returns the rectangle area"""
        return (self.width * self.heigth)

    def perimeter(self):
        """Public instance method, that returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

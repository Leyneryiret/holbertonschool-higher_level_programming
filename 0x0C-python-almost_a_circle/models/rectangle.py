#!/usr/bin/python3
""" module to create child class of Base """


from models.base import Base


class Rectangle(Base):
    """ new class of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Method that returns the width private of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """ Method that returns the height private of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ Method that returns the x private of the Rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ Method that returns the y private of the Rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

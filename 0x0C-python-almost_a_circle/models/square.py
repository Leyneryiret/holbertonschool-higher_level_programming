#!/usr/bin/python3

""" module to create child class of Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ new class Square  that inherits from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Method that returns the width private of the Rectangle """
        return self.__width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        else:
            self.__width = value
            self.__height = value


    def __str__(self):
        return "[Square] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
    

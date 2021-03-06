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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the height private of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Method that returns the x private of the Rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Method that returns the y private of the Rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public instance method, that returns the rectangle area"""
        return (self.width * self.height)

    def display(self):
        """Public instance method, that returns the rectangle display """
        for a in range(self.y):
            print()
        for i in range(self.height):
            for b in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute. """
        if (args):
            if (len(args) >= 1):
                self.id = args[0]
            if (len(args) >= 2):
                self.width = args[1]
            if (len(args) >= 3):
                self.height = args[2]
            if (len(args) >= 4):
                self.x = args[3]
            if (len(args) >= 5):
                self.y = args[4]
        elif (kwargs):
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the class dictionary. """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

#!/usr/bin/python3
""" Rectangle
Define the class Rectangle
    """


class Rectangle:
    """ Class rectangle that defines a
    rectangle by: (based on 8-rectangle.py)"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize the rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    """Public instance method, that returns the rectangle area"""
    def area(self):
        return (self.width * self.height)

    """Public instance method, that returns the rectangle perimeter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    """ __str__ method to print the Rectangle """
    def __str__(self):
        impri = ""
        if self.height == 0 or self.width == 0:
            return (impri)
        for i in range(self.height):
            for j in range(self.width):
                impri += str(self.print_symbol)
            impri += "\n"
        impri = impri[:-1]
        return (impri)

    """ Extract the representation of the rectangle with repr """
    def __repr__(self):
        rep = "Rectangle({self.width}, {self.height})".format(self=self)
        return rep

    """print a message when an instance is deleted"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

        """Static method that returns the biggestrectangle based on the area
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    """ Class method to create a square using the rectangle class """
    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

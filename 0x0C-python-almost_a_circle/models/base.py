#!/usr/bin/python3
""" Create, Base, the base of all other classes """

class Base:
    """ base” of all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        """ Method that returns the id of the Base """
        return self.__id

    @id.setter
    def id(self, value):
        if value == None:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
        else:
            self.__id = value

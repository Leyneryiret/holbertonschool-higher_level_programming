#!/usr/bin/python3

""" Módulo con una clase MyList para explorar la herencia """


class MyList(list):
    """ Define a class thar inherits from list """

    def __init__(self):
        self.MyList = []

    def print_sorted(self):
        """ Order the list """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)

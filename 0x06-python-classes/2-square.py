#!/usr/bin/python3
"""Creating a new class called Square"""


class Square:
    """class Square that defines a square by: (based on 0-square.py)"""
    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        try:
            self.__size = size
        except TypeError:
            print(size must be an integer)
        except ValueError:
            print(size must be >= 0)

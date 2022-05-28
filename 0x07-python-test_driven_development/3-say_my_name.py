#!/usr/bin/python3
"""
Function that prints My name is followed by:
<first name> and <last_name>
both of them should be a string, otherwhise a TypeError will raised
"""


def say_my_name(first_name, last_name=""):
        """Function that prints My name is followed by:
        <first name> and <last_name>
        both of them should be a string, otherwhise a TypeError will raised"""

        if type(first_name) != str:
                raise TypeError("first_name must be a string")

        if type(last_name) != str:
                raise TypeError("last_name must be a string")

        print("My name is", first_name, last_name)

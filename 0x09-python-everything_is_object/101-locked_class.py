#!/usr/bin/python3
"""this is the LockedClass module"""


class LockedClass:
    """special class prevents the user from dynamically
    ycreating new instance attributes,
    except if the new instance attribute is called first_name"""

    __slots__ = ['first_name']

    def __init___(self, first_name=""):
        self.first_name = first_name

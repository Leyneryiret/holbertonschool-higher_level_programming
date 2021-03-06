#!/usr/bin/python3
"""json to string"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file"""
    with open(filename, 'w') as f:
        txt = json.dumps(my_obj)
        f.write(txt)

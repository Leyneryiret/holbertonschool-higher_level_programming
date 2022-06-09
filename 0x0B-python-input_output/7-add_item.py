#!/usr/bin/python3
"""adds all arguments"""


import os.path
import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

python_list = []

if os.path.exists('./add_item.json'):
    python_list = load('add_item.json')

save(python_list + args, 'add_item.json')

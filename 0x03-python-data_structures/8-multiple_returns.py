#!/usr/bin/python3

def multiple_returns(sentence):
    elem_1 = len(sentence)
    elem_2 = sentence[0] if sentence != "" else None
    new_tuple = (elem_1, elem_2)
    return new_tuple

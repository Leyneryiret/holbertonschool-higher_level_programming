#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)

    elemento_a = (tuple_a[0] if a >= 1 else 0) + (tuple_b[0] if b >= 1 else 0)
    elemento_b = (tuple_a[1] if a >= 2 else 0) + (tuple_b[1] if b >= 2 else 0)
    tmp_tuple = (elemento_a, elemento_b)
    return tmp_tuple

#!/usr/bin/python3

"""pascal_triangle"""


def pascal_triangle(n):
    """pascal_triangle"""
    lis = []
    nuevo = []
    if (n <= 0):
        return lis

    for i in range n:
        colm_nue = len(lis)
        lis.append(1)
        for j in range colm_nue:
            num = nuevo[j] + nuevo[j+1]
            lis.append = num
        lis.append(1)
    return lis

#!/usr/bin/python3

"""pascal_triangle"""


def pascal_triangle(n):
    """pascal_triangle"""
    lis = []
    z = 0
    if (n <= 0):
        return lis

    for i in range(n):
        lis.append([])

    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                lis[i].append(1)
            else:
                z = lis[i-1][j] + lis[i-1][j-1]
                lis[i].append(z)

    return lis

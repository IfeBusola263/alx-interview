#!/usr/bin/python3
"""
This module implements the Pascal's triangle
"""
from math import factorial


def pascal_triangle(n):
    """
    The Pascal's triangle implementation.
    """

    if n <= 0:
        return []

    outerArr = []

    for i in range(n):
        innerArr = []
        for r in range(i + 1):
            ncr = factorial(i) // (factorial(r) * factorial(i-r))
            innerArr.append(ncr)
        outerArr.append(innerArr)
    return outerArr

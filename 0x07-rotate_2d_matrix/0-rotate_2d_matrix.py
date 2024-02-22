#!/usr/bin/python3
"""
This module houses a function that rotates a matrix.
"""


def rotate_2d_matrix(matrix):
    """
    This method rotates an nxn matrix inplace, without
    extra space comnsumed. It returns nothing.
    """
    for i in range(len(matrix[0])):
        for row in matrix:
            matrix[i].append(row.pop(i))
            row.insert(i, 0)

    for row in matrix:
        row.reverse()
        while 0 in row:
            row.remove(0)

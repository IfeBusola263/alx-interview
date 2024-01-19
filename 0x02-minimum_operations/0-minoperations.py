#!/usr/bin/env python3
'''
This module houses a function for minimum operation in a
file.
'''


def minOperations(n):
    '''
    Returns the minimum operation to achieve a number(n) of 'H'
    characters in a file. The only two operations are 'Copy All'
    and 'Paste'
    '''
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1
    current_length = 1

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 1

        current_length += clipboard
        operations += 1

    return operations

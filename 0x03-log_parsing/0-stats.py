#!/usr/bin/python3
'''
This script gets the standard input and outputs a statistics
in every ten lines or when a keyboard interupt input is executed.
'''

import sys

counter = 0
counter_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
    }

total_size = 0


def printer():
    '''
    This function prints the output of
    the statistics accumulated.
    '''
    print(f"File size: {total_size}")
    for status, numReq in counter_dict.items():
        if numReq > 0:
            print(f"{status}: {numReq}")


try:
    for line in sys.stdin:
        line_tup = line.split()
        counter += 1

        # if len(line_tup) == 9:
        try:
            file_size = int(line_tup[-1])
            total_size += file_size
        except (IndexError, ValueError, TypeError):
            continue

        try:
            status_code = line_tup[-2]
            if status_code in counter_dict.keys():
                counter_dict[status_code] = counter_dict.get(
                    status_code) + 1
            else:
                continue
        except (IndexError, ValueError, TypeError):
            continue

        if counter == 10:
            printer()
            counter = 0
    printer()
except KeyboardInterrupt:
    printer()
    raise

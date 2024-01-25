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


def printer(count_dict, size):
    '''
    This function prints the output of
    the statistics accumulated.
    '''
    print(f"File size: {size}")
    for status, numReq in count_dict.items():
        if numReq > 0:
            print(f"{status}: {numReq}")


try:
    for line in sys.stdin:
        line_tup = line.split(" ")
        # if len(line_tup) == 9:
        try:
            status_code = line_tup[7]
            fs = line_tup[8][:-1]
            file_size = int(fs)
            if status_code in counter_dict.keys():
                counter_dict[status_code] = counter_dict.get(
                    status_code) + 1
            total_size += file_size
            counter += 1
        except (IndexError, ValueError, TypeError):
            continue
        if counter == 10:
            printer(counter_dict, total_size)
            counter = 0
except KeyboardInterrupt:
    printer(counter_dict, total_size)

#!/usr/bin/python3
'''
This module parses log information
and prints it.
'''

import sys
import re


def process_line(line, metrics):
    # Define the regex pattern for extracting relevant information
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)')
    match = pattern.match(line)

    if match:
        ip_address, status_code, file_size = match.groups()
        # print(ip_address)
        # print(status_code)
        # print(file_size)
        metrics['total_size'] += int(file_size)

        if status_code in metrics['status_codes']:
            metrics['status_codes'][status_code] += 1


def print_metrics(metrics):
    '''
    Print out the metrics for the info collected
    on each successful parse.
    '''
    print(f"File size: {metrics['total_size']}")
    # print(metrics)
    # Print number of lines by status code in ascending order
    for status_code in sorted(metrics['status_codes']):
        if metrics['status_codes'][status_code] > 0:
            print(f"{status_code}: {metrics['status_codes'][status_code]}")


def main():
    metrics = {'total_size': 0,
               'status_codes': {
                   "200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0,
               }
               }
    line_count = 0

    try:
        for line in sys.stdin:
            process_line(line.strip(), metrics)
            line_count += 1

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print_metrics(metrics)
                # metrics = {'total_size': 0, 'status_codes': {}}

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_metrics(metrics)
        sys.exit(0)


if __name__ == "__main__":
    main()

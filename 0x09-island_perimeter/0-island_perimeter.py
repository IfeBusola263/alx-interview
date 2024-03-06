#!/usr/bin/python3
"""
This module has a function that calulates the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Returns the Perimeter of an island. The island is represented as
    a nested list, to form a rectangular shaped island.

    >>> grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    >>> print(island_perimeter(grid))
    12
    """

    if grid and isinstance(grid, list):
        height = 0
        firstOccur = 0
        lastOccur = 0
        flag = 0

        for section in grid:
            if 1 in section:
                height += 1
                if flag == 0:
                    firstOccur = section.index(1)
                    lastOccur = len(section) - 1 - section[::-1].index(1)
                    flag = 1
                else:
                    if firstOccur > section.index(1):
                        firstOccur = section.index(1)
                    if lastOccur < len(section) - 1 - section[::-1].index(1):
                        lastOccur = len(section) - 1 - section[::-1].index(1)
                # blockWidth = section.count(1)
                # if blockWidth > width:
                # width = blockWidth
        if firstOccur == 0:
            lastOccur += 1

        return (height + lastOccur) * 2

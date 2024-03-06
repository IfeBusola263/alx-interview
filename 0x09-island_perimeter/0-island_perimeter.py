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
        width = 0

        for section in grid:
            if 1 in section:
                height += 1
                blockWidth = section.count(1)
                if blockWidth > width:
                    width = blockWidth
        return (height + width) * 2

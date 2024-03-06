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
        # height = 0
        # width = 0

        # for section in grid:
        #     if 1 in section:
        #         height += 1
        #         blockWidth = section.count(1)
        #         if blockWidth > width:
        #             width = blockWidth
        # return (height + width) * 2

        height = len(grid)
        width = len(grid[0]) if height > 0 else 0

        perimeter = 0

        for i in range(height):
            for j in range(width):

                # checking individual cells
                if grid[i][j] == 1:
                    perimeter += 4

                    # If the cell has a neighbor above a value of 1
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    # If the cell has a neighbor to the left a value of 1
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter

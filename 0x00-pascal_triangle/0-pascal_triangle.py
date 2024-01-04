#!/usr/bin/python3
"""
This implements the Pascal's triangle.
"""

# def pascal_triangle(n):
#     """
#     The Pascal's triangle implementation.
#     """

#     if n <= 0:
#         return []

#     outerArr = []

#     for i in range(n):
#         innerArr = []
#         for r in range(i + 1):
#             ncr = factorial(i) // (factorial(r) * factorial(i-r))
#             innerArr.append(ncr)
#         outerArr.append(innerArr)
#     return outerArr


def calculate_factorial(num):
    """Calculate the factorial of a number."""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    outerArr = []

    for i in range(n):
        innerArr = []
        for r in range(i + 1):
            ncr = calculate_factorial(i) // (
                calculate_factorial(r) * calculate_factorial(i - r))
            innerArr.append(ncr)
        outerArr.append(innerArr)

    return outerArr

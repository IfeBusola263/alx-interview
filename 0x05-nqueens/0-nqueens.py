#!/usr/bin/python3
'''
This module houses functions that prints the
solutions for a chess board with a number of
Queens, in a way they do not attack each other.
'''
import sys


def is_safe(board, row, col, N):
    '''
    The function checks if it is safe to put a queen in
     a spot.
    '''

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][1] == col or abs(board[i][0] - row) == abs(
                board[i][1] - col):
            return False

    return True


def solve_nqueens(N):
    '''
    Entry point of the program, to validate and check input.
    '''

    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []

    def solve(board, row):
        '''
        This function put the queens in the right position
        where they are not attacked.
        '''

        if row == N:
            solutions.append(board[:])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = [row, col]
                solve(board, row + 1)

    solve([[0, 0]] * N, 0)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solutions = solve_nqueens(sys.argv[1])
    for solution in solutions:
        print(solution)
        # print()

#!/usr/bin/python3
""" Module to solve the n queens interview qustion """
import sys


def is_safe(row, col, queens):
    """ Makes sure that this queen placement is safe"""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queens=[], solutions=[]):
    """ Functions that recursevly places non-attacking queens
        On a NxN chessboard
    """
    if row == n:
        solutions.append(queens.copy())
        return

    for col in range(n):
        if is_safe(row, col, queens):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def main():
    """ Main function to handle sys args """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, solutions=solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

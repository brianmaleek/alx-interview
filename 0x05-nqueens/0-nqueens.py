#!/usr/bin/python3
"""
- Description: The N queens puzzle is the challenge of placing N non-attacking
        queens on an N×N chessboard. Write a program that solves the N queens
        problem.
            -  Usage: nqueens N
            - If the user called the program with wrong number of arguments,
            print Usage: nqueens N, followed by a new line, and exit with the
            status 1
            - where N must be an integer greater or equal to 4
            - If N is not an integer, print N must be a number, followed by a
                new line, and exit with the status 1
            - If N is smaller than 4, print N must be at least 4, followed by
                a new line, and exit with the status 1
            - The program should print every possible solution to the problem
            - One solution per line
            - Format: see example (check README file)
            - You don’t have to print the solutions in a specific order
            - You are only allowed to import the sys module
"""


import sys


def is_safe(queens, row, col):
    """
    - Check if it's safe to place a queen at the given position.

    Args:
        - queens (list): List of tuples representing positions of queens
            [(row1, col1), (row2, col2), ...]
        - row (int): Row index to check
        - col (int): Column index to check

    Returns:
        - bool: True if it's safe to place a queen at the given position,
            False otherwise
    """
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens_util(N, queens, row, solutions):
    """
    - Recursive backtracking function to find all possible solutions for the
            N Queens problem.

    Args:
        - N (int): Size of the chessboard
        - queens (list): List of tuples representing positions of queens
            [(row1, col1), (row2, col2), ...]
        - row (int): Current row being considered
        - solutions (list): List to store solutions found
    """
    if row == N:
        solutions.append(queens[:])
        return

    for col in range(N):
        if is_safe(queens, row, col):
            queens.append((row, col))
            solve_nqueens_util(N, queens, row + 1, solutions)
            queens.pop()


def solve_nqueens(N):
    """
    - Solve the N Queens problem and print all possible solutions.

    Args:
        - N (str): Size of the chessboard and number of queens

    Raises:
        - ValueError: If N is not an integer or less than 4
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens_util(N, [], 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        solve_nqueens(sys.argv[1])
    except ValueError as e:
        print(e)
        sys.exit(1)

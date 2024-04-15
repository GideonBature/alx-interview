#!/usr/bin/python3
import sys


def print_usage():
    """print usage"""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid_position(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """ Use backtracking to solve the problem
    """
    if col >= len(board):
        # All queens are placed
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    """Consider this column and try placing this queen
    in all rows one by one
    """
    for i in range(len(board)):
        if is_valid_position(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0  # backtrack


def main():
    """The main function
    """
    if len(sys.argv) != 2:
        print_usage()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0] * n for _ in range(n)]
    global solutions
    solutions = []

    # Solve the N Queens problem
    solve_nqueens(board, 0)

    # Print all solutions found
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

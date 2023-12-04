def is_valid(board, row, col, num):
    # Check if the number can be placed in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number can be placed in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    # Find an empty cell
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        # No empty cell, the Sudoku is solved
        return True

    row, col = empty_cell

    # Try placing numbers 1 through 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number if it's valid
            board[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing the current number doesn't lead to a solution, backtrack
            board[row][col] = 0

    # No number from 1 to 9 can be placed in this cell, backtrack
    return False

def find_empty_cell(board):
    # Find the first empty cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku Solved:")
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")

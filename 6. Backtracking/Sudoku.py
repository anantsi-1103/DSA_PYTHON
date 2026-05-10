def isSafe(board, row, col, num):
    
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3×3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


def solve_sudoku(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if isSafe(board, row, col, num):

                        # Place number
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        # Backtrack
                        board[row][col] = 0

                
                return False

   
    return True


board = [
    [3,0,6,5,0,8,4,0,0],
    [5,2,0,0,0,0,0,0,0],
    [0,8,7,0,0,0,0,3,1],
    [0,0,3,0,1,0,0,8,0],
    [9,0,0,8,6,3,0,0,5],
    [0,5,0,0,9,0,6,0,0],
    [1,3,0,0,0,0,2,5,0],
    [0,0,0,0,0,0,0,7,4],
    [0,0,5,2,0,6,3,0,0]
]
solve_sudoku(board)

if solve_sudoku(board):
    print("Solved Sudoku:\n")

    for row in board:
        print(row)
else:
    print("No solution exists")
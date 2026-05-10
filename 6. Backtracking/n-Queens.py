
def isSafe(board , row, col , n):

    # check column - vertical
    for i in range(row):
        if(board[i][col] == 1):
            return False


    # check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if(board[i][j] == 1):
            return False
        i-=1
        j-=1

    # check right diagonal
    i = row - 1
    j = col + 1


    while i >= 0 and j < n:
        if(board[i][j] == 1):
            return False
        i-=1
        j+=1

    return True

def solve_n_queen(board , row, n):
    # base case
    if(row == n):
        printBoard(board,n)
        return
    

    for col in range(n):
        # 0 
        if isSafe(board, row,col, n):

            # place queen
            board[row][col] = 1

            # Move to next row
            solve_n_queen(board , row+1, n)

            # Backtrack
            board[row][col] = 0


def printBoard(board, n):
    # row
    for i in range(n):
        for j in range(n):
            # 
            if(board[i][j] == 1):
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()





n = 4
# nested list of loop -> 2d -> 4x4 -> 0
board = [[0]*n for _ in range(n)]


solve_n_queen(board , 0, n)
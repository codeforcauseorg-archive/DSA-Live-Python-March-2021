def nqueens(board, row):

    if row == len(board):
        return 1

    count = 0

    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = True
            count += nqueens(board, row+1)
            board[row][col] = False

    return count

def isSafe(board, row, col):

    for index in range(1, row+1):
        if board[row-index][col]:
            return False

        if (col-index >= 0) and board[row-index][col-index]:
            return False

        if (col+index <len(board)) and board[row-index][col+index]:
            return False

    return True


n = 6

board = []

for i in range(n):
    board.append([False] * n)

out = nqueens(board, 0)

print(out)






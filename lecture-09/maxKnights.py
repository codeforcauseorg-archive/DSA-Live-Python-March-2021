def maxnights(board, row, col, knights):

    if row == len(board):
        return knights

    if col == len(board):
        return maxnights(board, row+1, 0, knights)

    [left, right] = [0, 0]

    if isSafe(board, row, col):
        board[row][col] = True
        left = maxnights(board, row, col+1, knights+1)
        board[row][col] = False

    right = maxnights(board, row, col+1, knights)

    return max(left, right)


def isSafe(board, row, col):

    if ((row-1) >= 0) and ((col-2) > 0) and board[row-1][col-2]:
        return False

    if ((row-2) >= 0) and ((col-1) > 0) and board[row-2][col-1]:
        return False

    if ((row-2) >= 0) and ((col+1) < len(board)) and board[row-2][col+1]:
        return False

    if ((row-1) >= 0) and ((col+2) < len(board)) and board[row-1][col+2]:
        return False

    return True


n = 3

board = []

for i in range(n):
    board.append([False] * n)

out = maxnights(board, 0, 0, 0)

print(out)






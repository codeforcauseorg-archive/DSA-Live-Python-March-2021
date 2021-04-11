def maze(board, cx, cy, tx, ty, rows, cols, path=""):

    if(cx < 0 or cx >= rows or cy < 0 or cy >= cols):
        return

    if(board[cx][cy]):
        return

    if(cx == tx and cy == ty):
        print(path)
        return

    board[cx][cy] = True
    maze(board, cx-1, cy, tx, ty, rows, cols, path+"N")
    maze(board, cx, cy+1, tx, ty, rows, cols, path+"E")
    maze(board, cx+1, cy, tx, ty, rows, cols, path+"S")
    maze(board, cx, cy-1, tx, ty, rows, cols, path+"W")
    board[cx][cy] = False


rows = 4
cols = 4

board = []

for row in range(rows):
    board.append([False] * cols)


maze(board, 3, 3, 2, 2, rows, cols, "")



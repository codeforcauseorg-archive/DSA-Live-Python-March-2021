grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]



def sudoku(grid, row, col):

    if row == 9:
        for line in grid:
            print(line)
        return

    if col == 9:
        sudoku(grid, row+1, 0)
        return

    if grid[row][col] == 0:
        for value in range(1, 10):
            if(isSafe(grid, row, col, value)):
                grid[row][col] = value
                sudoku(grid, row, col+1)
                grid[row][col] = 0
    else:
        sudoku(grid, row, col + 1)


def isSafe(grid, row, col, value):

    # check col
    for r in range(9):
        if(grid[r][col] == value):
            return False

    # check row
    for c in range(9):
        if (grid[row][c] == value):
            return False


    # check grid
    cr = row - (row%3)
    cc = col - (col%3)
    for r in range(cr, cr+3):
        for c in range(cc, cc+3):
            if grid[r][c] == value:
                return False

    return True


sudoku(grid, 0, 0)






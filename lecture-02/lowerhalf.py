n = 4

row = 0
while row < n:
    c_mirr = 0
    col = 0
    while c_mirr < 2 * n - 1:
        if(col < row):
            print(" ", end=" ")
        else:
            print("*", end=" ")

        if c_mirr < n-1:
            col += 1
        else:
            col -= 1

        c_mirr += 1

    print()
    row += 1
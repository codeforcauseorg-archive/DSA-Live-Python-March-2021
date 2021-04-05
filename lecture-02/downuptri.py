n = 4

r_mirr = 0
row = 0
while r_mirr < 2 * n - 1:
    col = 0
    while col < n - row:
        print("*", end=" ")
        col += 1

    print()

    if r_mirr < n - 1:
        row += 1
    else:
        row -= 1

    r_mirr += 1
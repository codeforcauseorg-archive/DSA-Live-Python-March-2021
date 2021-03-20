n = 4

row = 0
while row < n:
    col = 0
    while col < n - row:
        print("*", end=" ")
        col += 1

    print()
    row += 1
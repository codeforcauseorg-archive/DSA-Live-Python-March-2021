n = 10

row = 0
while row < n:
    col = 0
    while col <= row:
        print("*", end=" ")
        col += 1

    row += 1
    print()

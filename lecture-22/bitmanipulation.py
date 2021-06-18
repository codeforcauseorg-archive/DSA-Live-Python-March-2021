n = 6

count = 0

while n > 0:

    if n & 1 == 0:
        n = n >> 1
    else:
        n = n ^ 1

    count += 1

print(count)
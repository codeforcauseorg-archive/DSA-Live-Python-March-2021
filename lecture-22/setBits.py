n = 100

count = 0

while n > 0:
    count += (n & 1)
    n = n >> 1

print(count)
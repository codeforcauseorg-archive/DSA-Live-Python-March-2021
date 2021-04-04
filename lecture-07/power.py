# power(x, y) where x and y are int and y is >= 0

def power(x, y):
    if y == 0:
        return 1

    subrec = power(x, y-1)
    output = x * subrec
    return output

print(power(3, 5))

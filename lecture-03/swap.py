a = 10
b = 20

# this will not work
def swap(x, y):
    temp = x
    x = y
    y = temp

swap(a, b)

print(a, b)
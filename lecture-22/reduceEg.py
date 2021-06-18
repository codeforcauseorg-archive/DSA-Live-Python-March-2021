from  functools import reduce

li = [2, 4, 5, 6, 7]

# print(list(map(lambda x: x*x, li)))
# print(list(filter(lambda x: x > 5, li)))


def summer(a, b):
    print(a, b)
    return a^b


print(reduce(summer, li, 0))


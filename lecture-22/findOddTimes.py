from functools import reduce

nums = [1, 2, 1, 3, 2]

print(reduce(lambda a, b: a^b, nums, 0))
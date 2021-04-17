import random

def quickSort(nums, start, end):

    if start >= end:
        return

    p = pivot(nums, start, end)

    quickSort(nums, start, p-1)
    quickSort(nums, p+1, end)

def pivot(nums, start, end):

    p = end
    j = start

    for i in range(start, end):
        if nums[i] < nums[p]:
            swap(nums, i, j)
            j += 1

    swap(nums, p, j)

    return j

def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t


items = []

for i in range(30):
    items.append(random.randint(10, 40))

print(items)

quickSort(items, 0, len(items)-1)
print(items)
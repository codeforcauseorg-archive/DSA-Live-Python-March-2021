import random

def mergeSort(nums):

    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = nums[0:mid]
    right = nums[mid:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    return merge(sortedLeft, sortedRight)


def merge(first, second):

    result = []

    i, j = 0, 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    while i < len(first):
        result.append(first[i])
        i += 1

    while j < len(second):
        result.append(second[j])
        j += 1

    return result


items = []

for i in range(30):
    items.append(random.randint(10, 40))

print(items)
print(mergeSort(items))


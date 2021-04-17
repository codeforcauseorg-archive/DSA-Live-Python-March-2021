def pivot(nums, start, end):

    p = end
    j = start

    for i in range(start, end):
        if nums[i] > nums[p]:
            swap(nums, i, j)
        else:
            j += 1

    swap(nums, p, j)

    return j

def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t




li = [8, 10, 78, 65, 45, 47, 56, 34, 19]

def swap(nums, src, tgt):
    temp = nums[src]
    nums[src] = nums[tgt]
    nums[tgt] = temp

def insertion(nums):

    for i in range(0, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                swap(nums, j, j-1)
            else:
                break

insertion(li)

print(li)


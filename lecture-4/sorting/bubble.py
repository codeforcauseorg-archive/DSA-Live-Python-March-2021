li = [8, 10, 78, 65, 45, 47, 56, 34, 19]


def swap(nums, src, tgt):
    temp = nums[src]
    nums[src] = nums[tgt]
    nums[tgt] = temp

def bubble(nums):

    for row in range(0, len(nums)):
        for idx in range(0, len(nums) - row - 1):
            if nums[idx] > nums[idx + 1]:
                swap(nums, idx, idx+1)

bubble(li)

print(li)
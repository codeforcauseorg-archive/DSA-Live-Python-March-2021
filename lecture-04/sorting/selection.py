li = [10, 78, 65, 45, 47, 8, 56, 34, 19]

def swap(nums, src, tgt):
    temp = nums[src]
    nums[src] = nums[tgt]
    nums[tgt] = temp

def maxIndex(nums, start, end):

    maxIdx = start

    for idx in range(start+1, end+1):
        if(nums[idx] > nums[maxIdx]):
            maxIdx = idx

    return maxIdx

def selection(nums):
    for itr in range(0, len(nums)):
        maxIdx = maxIndex(nums, 0, len(nums)-itr-1)
        swap(nums, maxIdx, len(nums)-itr-1)

selection(li)
print(li)
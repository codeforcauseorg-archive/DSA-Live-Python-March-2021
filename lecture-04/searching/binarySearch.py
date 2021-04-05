li = [10, 78, 65, 45, 47, 8, 56, 34, 19]

li.sort()

print(li)

def binarySearch(nums, value):
    start = 0
    end = len(nums) - 1

    while(start <= end):
        mid = (start + end) // 2

        if(nums[mid] == value):
            return mid
        elif value < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None




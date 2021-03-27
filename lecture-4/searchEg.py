li = [10, 78, 65, 45, 47]

# print(li.index(47))

def linearSearch(nums, value):

    for i in range(0, len(nums)):
        if nums[i] == value:
            return i

    return None

print(linearSearch(li, 78))


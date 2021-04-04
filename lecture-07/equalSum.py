def equalSum(complete, left=[], right=[]):
    if(len(complete) == 0):
        if(sum(left) == sum(right)):
            print(left, right)
        return

    current = complete[0]
    remaining = complete[1:]

    equalSum(remaining, left+[current], right)
    equalSum(remaining, left, right+[current])


equalSum([1, 2, 3])
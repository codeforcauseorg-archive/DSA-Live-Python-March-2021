def equalSum(complete, index=0,  left=[], right=[]):
    if(len(complete) == index):
        if(sum(left) == sum(right)):
            print(left, right)
        return

    current = complete[index]

    equalSum(complete, index+1, left+[current], right)
    equalSum(complete, index+1, left, right+[current])


equalSum([1, 2, 3])
def equalSum(complete, index=0,  left=[], right=[]):
    if(len(complete) == index):
        if(sum(left) == sum(right)):
            print(left, right)
        return

    current = complete[index]

    left.append(current)
    equalSum(complete, index+1, left, right)
    left.pop()

    right.append(current)
    equalSum(complete, index+1, left, right)
    right.pop()


equalSum([1, 2, 3])
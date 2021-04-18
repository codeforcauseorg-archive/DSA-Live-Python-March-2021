def dice(target, faces):

    if target == 0:
        return 1

    count = 0

    for face in range(1, faces+1):
        if face <= target:
            count += dice(target-face, faces)

    return count


def diceDP(target, faces, memoryList):

    if target == 0:
        return 1

    if memoryList[target] != None:
        return memoryList[target]

    count = 0
    for face in range(1, faces+1):
        if face <= target:
            count += diceDP(target-face, faces, memoryList)

    memoryList[target] = count
    return count


def diceDPIter(target, faces):

    memoryList = [None] * (target + 1)

    for t in range(0, target + 1):

        if t == 0:
            memoryList[t] = 1
        else:
            count = 0
            for face in range(1, faces+1):
                if face <= t:
                    count += memoryList[t-face]
            memoryList[t] = count

    return memoryList[target]

# target = 800
# memoryList = [None] * (target+1)
# out = diceDP(target, 4, memoryList)
# print(out)

print(diceDPIter(100000, 4))

# print(dice(50, 4))


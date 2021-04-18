def fibo(num):
    if num < 2:
        return num

    result = fibo(num-1) + fibo(num-2)
    return result


def fiboDP(num, memory):
    if num < 2:
        return num

    if num in memory:
        return memory[num]

    result = fiboDP(num-1, memory) + fiboDP(num-2, memory)
    memory[num] = result
    return result


def fiboDPList(num, memoryList):
    if num < 2:
        return num

    if memoryList[num] != None:
        return memoryList[num]

    result = fiboDPList(num-1, memoryList) + fiboDPList(num-2, memoryList)
    memoryList[num] = result
    return result


def fiboDPIter(number):

    memoryList = [None] * (number + 1)

    for num in range(0, number + 1):
        if num < 2:
            memoryList[num] = num
        else:
            result = memoryList[num-1] + memoryList[num-2]
            memoryList[num] = result

    return memoryList[number]


# print(fiboDP(100, {}))
# num = 10
# memory = [None] * (num+1)
# # print(memory)
# print(fiboDPList(num, memory))

print(fiboDPIter(100000))

# memory = {7: 70}
#
# if 7 in memory:
#     print(memory[7])
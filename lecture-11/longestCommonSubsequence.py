def longestCommonSubsequence(text1, text2, len1, len2):

    if len1 == 0 or len2 == 0:
        return 0

    if text1[len1-1] == text2[len2-1]:
        out = 1 + longestCommonSubsequence(text1, text2, len1-1, len2-1)
    else:
        left = longestCommonSubsequence(text1, text2, len1, len2-1)
        right = longestCommonSubsequence(text1, text2, len1-1, len2)
        out = max(left, right)

    return out


def longestCommonSubsequenceDP(text1, text2, len1, len2, memoryList):

    if len1 == 0 or len2 == 0:
        return 0

    if memoryList[len1][len2] != None:
        return memoryList[len1][len2]

    if text1[len1-1] == text2[len2-1]:
        out = 1 + longestCommonSubsequenceDP(text1, text2, len1-1, len2-1, memoryList)
    else:
        left = longestCommonSubsequenceDP(text1, text2, len1, len2-1, memoryList)
        right = longestCommonSubsequenceDP(text1, text2, len1-1, len2, memoryList)
        out = max(left, right)

    memoryList[len1][len2] = out

    return out


def longestCommonSubsequenceDPIter(text1, text2):

    memList = []
    for i in range(len(text1) + 1):
        memList.append([None] * (len(text2) + 1))

    for len1 in range(len(text1)+1):
        for len2 in range(len(text2)+1):
            if len1 == 0 or len2 == 0:
                memList[len1][len2] = 0
            else:
                if text1[len1 - 1] == text2[len2 - 1]:
                    out = 1 + memList[len1 - 1][len2 - 1]
                else:
                    left = memList[len1][len2 - 1]
                    right = memList[len1 - 1][len2]
                    out = max(left, right)

                memList[len1][len2] = out

    return memList[len(text1)][len(text2)]



first = "aman"
second = "manan"

memList = []
for i in range(len(first) + 1):
    memList.append([None] * (len(second)+1))

print(longestCommonSubsequenceDP(first, second, len(first), len(second), memList))


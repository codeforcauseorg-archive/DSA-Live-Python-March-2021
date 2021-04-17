first = [1, 3, 6, 8, 10]

second = [3, 7, 11, 13]

def merge(first, second):

    result = []

    i, j = 0, 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    while i < len(first):
        result.append(first[i])
        i += 1

    while j < len(second):
        result.append(second[j])
        j += 1

    return result


out = merge(first, second)

print(out)


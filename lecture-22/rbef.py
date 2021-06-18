li = [1, 2, 3, 5, 1, 2, 4, 3]

for i in range(1, len(li)):
    li[i] = li[i-1] ^ li[i]


for i in range(len(li)):
    for k in range(i+1, len(li)):

        cxor = li[k]
        if i > 0:
            cxor = cxor ^ li[i-1]

        if cxor == 0:
            print(i, k)

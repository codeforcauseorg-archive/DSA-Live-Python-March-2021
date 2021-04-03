line = "aabbccdeefff"

freq = [0]*26
for ch in line:
    index = (ord(ch) - ord("a"))
    freq[index] += 1

for i in range(len(freq)):
    ch = chr(i + ord("a"))
    print(ch, freq[i])





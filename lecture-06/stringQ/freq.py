line = "here is our data"

freq = {}

for ch in line:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
        
print(freq)
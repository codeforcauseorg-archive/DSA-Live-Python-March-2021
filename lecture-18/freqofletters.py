line = "welcome to code for cause"

import string

lower = set(string.ascii_lowercase)

freq = {}
#
# for ch in line.lower():
#
#     if ch in lower:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1

vowels = set("aeiou")

for ch in line.lower():
    if ch in vowels:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

print(sorted(list(freq.items()), key=lambda x: x[1]))

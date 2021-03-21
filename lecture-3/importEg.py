import os

# print(os.path.exists("fnScope.py"))

os.makedirs("Hello")

counter = 1

while counter < 10:
    os.makedirs("Hello/Hello"+str(counter))
    counter += 1
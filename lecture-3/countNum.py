number = int(input("Enter a number : "))
d = int(input("Enter the digit to count : "))

# print((str(number).count("5")))

count = 0

while number > 0:
    digit = number % 10
    if digit == d:
        count += 1

    number = number // 10

print(count)
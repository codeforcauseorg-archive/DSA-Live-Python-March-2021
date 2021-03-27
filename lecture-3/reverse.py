number = int(input("Enter a number : "))

result = 0

negative = number < 0

number = abs(number)


while number > 0:
    digit = number % 10
    result = result * 10 + digit
    number = number // 10

if(negative):
    result = -result

print(result)
def factorial(n):

    if n == 0:
        return 1

    subrec = factorial(n-1)
    output = n * subrec
    return output


val = int(input("Enter number : "))
out = factorial(val)
print(out)
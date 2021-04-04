def fibo(n):
    if n < 2:
        return n

    left = fibo(n-1)
    right = fibo(n-2)
    output = left + right
    return output

print(fibo(4))
def pd(n):
    if n == 0:
        return

    pd(n-1)
    print(n)

pd(5)

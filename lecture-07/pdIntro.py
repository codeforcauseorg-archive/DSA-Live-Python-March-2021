# def pd5():
#     print(5)
#     pd4()
#     print("later 5")
#
# def pd4():
#     print(4)
#     pd3()
#     print("later 4")
#
# def pd3():
#     print(3)
#     pd2()
#     print("later 3")
#
# def pd2():
#     print(2)
#     pd1()
#     print("later 2")
#
# def pd1():
#     print(1)
#     pd0()
#     print("later 1")
#
# def pd0():
#     return
#
# pd5()

def pd(n):
    if n == 0:
        return

    print(n)
    pd(n-1)
    
    return

pd(5)

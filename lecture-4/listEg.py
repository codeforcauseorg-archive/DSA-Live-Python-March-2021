li = [[45, 56], [78, 89]]

another = li.copy()

print(li)
print(another)

print(li[0] is another[0])

li[0].append(20)



print(li)
print(another)

third = [li[0], li[1]]

third[0].append(60)

print(li)
print(another)
print(third)


# # li.append(10)
#
# print(li)
#
# print(li.count(10))

li
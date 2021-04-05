import json

li = [[45, 56], [78, 89]]

li_serial = json.dumps(li)

print(type(li_serial))

another = json.loads(li_serial)

print(li)
print(another)

li[0].append(10)

print(li)
print(another)
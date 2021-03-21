name = "Father"

def sayhello():
    global name
    name = "Mohit"
    print("Hello " + name)

sayhello()

print(name)
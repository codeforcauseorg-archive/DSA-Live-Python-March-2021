class CustomStack:

    def __init__(self):
        self.__data = list()

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        return self.__data.pop()

    def top(self):
        return self.__data[-1]

    def size(self):
        return len(self.__data)


stack = CustomStack()

stack.push(10)
stack.push(40)
stack.push(20)
stack.push(100)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

class CustomQueue:

    def __init__(self):
        self.__data = list()

    def insert(self, value):
        self.__data.append(value)

    def remove(self):
        return self.__data.pop(0)

    def front(self):
        return self.__data[0]

    def size(self):
        return len(self.__data)



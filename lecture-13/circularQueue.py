class CircularQueue:

    def __init__(self):
        self.__data = [None] * 10
        self.__front = 0
        self.__end = -1
        self.__size = 0

    def insert(self, value):

        if self.__size == len(self.__data):
            old = self.__data
            self.__data = [None] * (2*len(old))
            for i in range(len(old)):
                self.__data[i] = old[(self.__front + i) % len(old)]
                self.__front = 0
                self.__end = len(old) - 1

        self.__end = (1 + self.__end) % len(self.__data)
        self.__data[self.__end] = value
        self.__size += 1

    def delete(self):
        if self.__size == 0:
            return None

        value = self.__data[self.__front]
        self.__front = (self.__front + 1) % len(self.__data)
        self.__size -= 1
        return value

    def front(self):
        return self.__data[self.__front]

    def size(self):
        return self.__size


queue = CircularQueue()

for i in range(1000000):
    queue.insert(i)

for i in range(1000000):
    queue.delete()






class Node:

    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt


class CustomLinkedList:

    def __init__(self):
        self.__head = None
        self.__size = 0
        self.__tail = None

    def insertFirst(self, value):
        node = Node(value)
        node.nxt = self.__head
        self.__head = node
        self.__size += 1

        if self.__size == 1:
            self.__tail = self.__head


    def insertLast(self, value):
        if self.__size == 0:
            self.insertFirst(value)
            return

        node = Node(value)
        self.__tail.nxt = node
        self.__tail = node

        self.__size += 1

    def __getItem(self, index):

        node = self.__head
        for i in range(0, index):
            node = node.nxt

        return node

    def insertAt(self, value, index):

        if index == 0:
            self.insertFirst(value)
        elif index == self.__size:
            self.insertLast(value)
        else:
            prev = self.__getItem(index-1)
            node = Node(value)
            node.nxt = prev.nxt
            prev.nxt = node
            self.__size += 1

    def removeFirst(self):

        value = self.__head.value

        self.__head = self.__head.nxt
        self.__size -= 1

        if self.__size == 0:
            self.__tail = None

        return value

    def removeLast(self):
        if self.__size == 1:
            return self.removeFirst()

        value = self.__tail.value

        prev = self.__getItem(self.__size - 2)
        self.__tail = prev
        prev.nxt = None

        self.__size -= 1

        return value

    def removeFrom(self, index):
        if index == 0:
            return self.removeFirst()
        elif index == self.__size - 1:
            return self.removeLast()
        else:
            prev = self.__getItem(index-1)
            value = prev.nxt.value
            prev.nxt = prev.nxt.nxt
            self.__size -= 1
            return value

    def __repr__(self):
        output = []
        node = self.__head
        while node != None:
            output.append(node.value)
            node = node.nxt
        return "->".join(output)




ll = CustomLinkedList()
ll.insertFirst("Ravi")
ll.insertFirst("Priya")
ll.insertFirst("Shubham")

ll.insertLast("Nikita")
ll.insertLast("Khan")

print(ll)

ll.insertAt("Suraj", 1)

print(ll)

ll.removeFirst()

print(ll)

ll.removeFirst()

print(ll)

ll.removeLast()

print(ll)
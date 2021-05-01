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
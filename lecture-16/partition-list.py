# https://leetcode.com/problems/partition-list/submissions/

# Definition for singly-linked list.

class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LL:

    def __init__(self):

        self.head = None
        self.tail = None
        self.mid = None
        self.size = 0

    def pushFront(self, value):

        node = Node(value)
        node.next = self.head

        if self.size > 0:
            self.head.prev = node

        self.head = node

        self.size += 1

        if self.size == 1:
            self.tail = node
            self.mid = node
        elif (self.size % 2) == 0:
            self.mid = self.mid.prev


    def pushMiddle(self, value):

        if self.size <= 2:
            self.pushFront(value)
            return

        prev = self.mid.prev
        node = Node(value)
        node.next = prev.next
        node.prev = prev
        prev.next = node
        self.mid.prev = node

        self.size += 1

        if (self.size % 2) == 0:
            self.mid = self.mid.prev

    def pushEnd(self, value):

        if self.size == 0:
            self.pushFront(value)
            return

        node = Node(value)

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        self.size += 1

        if (self.size % 2) == 1:
            self.mid = self.mid.next

    def display(self):

        values = []
        node = self.head

        while node:
            values.append(node.value)
            node = node.next

        print(" => ".join([str(value) for value in values]))


ll = LL()

ll.pushFront(11)
ll.display()

ll.pushFront(22)
ll.display()

ll.pushFront(33)
ll.display()

ll.pushMiddle(44)
ll.display()

ll.pushMiddle(55)
ll.display()

ll.pushMiddle(66)
ll.display()

ll.pushEnd(88)
ll.display()










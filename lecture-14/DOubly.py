class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class FrontMiddleBackQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.mid = None

        self.size = 0

    def pushFront(self, val) :

        node = Node(val)
        node.next = self.head
        self.head.prev = node
        self.head = node

        self.size += 1

        if self.size == 1:
            self.tail = node
            self.mid = node
        else:
            if self.size % 2 == 1:
                self.mid = self.mid.next


    def pushMiddle(self, val):
        if self.size == 0:
            self.pushFront(val)
            return



    def pushBack(self, val) :

    def popFront(self) :

    def popMiddle(self) :

    def popBack(self) :

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
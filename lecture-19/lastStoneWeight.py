# https://leetcode.com/problems/last-stone-weight/submissions/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = MinHeap(compare=lambda first, second: second - first)

        for stone in stones:
            heap.insert(stone)

        while heap.size() > 1:
            heavy = heap.remove()
            light = heap.remove()

            if light < heavy:
                heap.insert(heavy - light)

        if heap.size() == 1:
            return heap.remove()
        else:
            return 0


class MinHeap:

    def __init__(self, compare=None):
        self.data = []

        if not compare:
            self.compare = lambda a, b: a - b
        else:
            self.compare = compare

    def insert(self, value):
        self.data.append(value)
        self.__upheap()

    def __upheap(self):
        index = len(self.data) - 1
        while index > 0:
            parent = self.parent(index)
            parentValue = self.data[parent]
            if self.compare(parentValue, self.data[index]) > 0:
                self.swap(index, parent)
                index = parent
            else:
                break

    def remove(self):
        value = self.data[0]
        last = self.data.pop()

        if len(self.data) > 0:
            self.data[0] = last
            self.__downheap()

        return value

    def __downheap(self):
        index = 0

        while index < len(self.data):
            left, right = self.left(index), self.right(index)
            minIndex = index

            if (left < len(self.data)) and (self.compare(self.data[left], self.data[minIndex]) < 0):
                minIndex = left

            if (right < len(self.data)) and (self.compare(self.data[right], self.data[minIndex]) < 0):
                minIndex = right

            if index != minIndex:
                self.swap(index, minIndex)
                index = minIndex
            else:
                break

    def swap(self, first, second):
        self.data[first], self.data[second] = self.data[second], self.data[first]

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return (2 * index) + 1

    def right(self, index):
        return (2 * index) + 2

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)





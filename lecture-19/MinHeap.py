import random

class MinHeap:

    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self.__upheap()

    def __upheap(self):
        index = len(self.data) - 1
        while index > 0:
            parent = self.parent(index)
            parentValue = self.data[parent]
            if parentValue > self.data[index]:
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

            if (left < len(self.data)) and (self.data[left] < self.data[minIndex]):
                minIndex = left

            if (right < len(self.data)) and (self.data[right] < self.data[minIndex]):
                minIndex = right

            if index != minIndex:
                self.swap(index, minIndex)
                index = minIndex
            else:
                break

    def swap(self, first, second):
        self.data[first], self.data[second] = self.data[second], self.data[first]

    def parent(self, index):
        return (index-1)//2

    def left(self, index):
        return (2*index) + 1

    def right(self, index):
        return (2*index) + 2

    def empty(self):
        return len(self.data) == 0

nums = []
heap = MinHeap()
for i in range(15):
    nums.append(random.randint(1, 30))

for val in nums:
    heap.insert(val)

result = []

while not heap.empty():
    result.append(heap.remove())

print(nums)
print(result)



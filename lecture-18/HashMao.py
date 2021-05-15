class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.key) + " : " + str(self.value)


class HashMap:

    def __init__(self):
        self.data = []
        self.size = 0
        for i in range(20):
            self.data.append([])

    def set(self, key, value):

        index = hash(key) % len(self.data)
        bucket = self.data[index]

        for node in bucket:
            if node.key == key:
                node.value = value
                return

        node = Node(key, value)
        bucket.append(node)
        self.size += 1

        if (self.size / len(self.data)) > 5:
            self.rehash()

    def rehash(self):
        old = self.data

        self.data = []
        for i in range(len(old)*2):
            self.data.append([])

        self.size = 0

        for bucket in old:
            for node in bucket:
                self.set(node.key, node.value)

    def get(self, key):

        index = hash(key) % len(self.data)
        bucket = self.data[index]

        for node in bucket:
            if node.key == key:
                return node.value
        return None

    def has(self, key):
        index = hash(key) % len(self.data)
        bucket = self.data[index]

        for node in bucket:
            if node.key == key:
                return True
        return False

    def remove(self, key):

        index = hash(key) % len(self.data)
        bucket = self.data[index]

        remove_index = None

        for index, node in enumerate(bucket):
            if node.key == key:
                remove_index = index
                break

        if remove_index != None:
            bucket.pop(remove_index)
            self.size -= 1


d = HashMap()

for i in range(100000):
    d.set(i, i)

# print(d.data)





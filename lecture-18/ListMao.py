class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.key) + " : " + str(self.value)

class ListMap:

    def __init__(self):
        self.data = []

    def set(self, key, value):

        for node in self.data:
            if node.key == key:
                node.value = value
                return

        node = Node(key, value)
        self.data.append(node)

    def get(self, key):

        for node in self.data:
            if node.key == key:
                return node.value
        return None

    def has(self, key):
        for node in self.data:
            if node.key == key:
                return True
        return False




d = ListMap()

for i in range(100000):
    d.set(i, i)



class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(value, self.root)

    def __insert(self, value, node):

        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self.__insert(value, node.left)
        elif value > node.value:
            node.right = self.__insert(value, node.right)

        return node

    def copy(self):
        newroot = self.__copy(self.root)

        newTree = BST()
        newTree.root = newroot

        return newTree

    def __copy(self, node):
        if not node:
            return None

        temp = Node(node.value)
        temp.left = self.__copy(node.left)
        temp.right = self.__copy(node.right)

        return temp




    def min(self):
        node = self.root
        if not node:
            return None

        while node.left:
            node = node.left

        return node.value

    def inorder(self):
        self.__inorder(self.root)
        print()

    def __inorder(self, node):
        if not node:
            return

        self.__inorder(node.left)
        print(node.value, end=" ")
        self.__inorder(node.right)

    def revinorder(self):
        self.__revinorder(self.root)

    def __revinorder(self, node):
        if not node:
            return

        self.__revinorder(node.right)
        print(node.value)
        self.__revinorder(node.left)



tree = BST()

tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(2)

# print(tree.min())

# tree.revinorder()

newT = tree.copy()

tree.inorder()
newT.inorder()

newT.insert(30)

tree.inorder()
newT.inorder()


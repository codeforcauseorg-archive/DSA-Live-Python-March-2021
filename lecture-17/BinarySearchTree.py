class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


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

        node.height = 1 + max(BST.height(node.left), BST.height(node.right))

        node = BST.avl(node)

        return node

    @classmethod
    def height(cls, node):
        if not node:
            return 0

        return node.height


    def __copy(self, node):
        if not node:
            return None

        temp = Node(node.value)
        temp.left = self.__copy(node.left)
        temp.right = self.__copy(node.right)

        return temp

    def inorder(self):
        self.__inorder(self.root)
        print()

    def __inorder(self, node):
        if not node:
            return

        self.__inorder(node.left)
        print(node.value, end=" ")
        self.__inorder(node.right)

    @classmethod
    def leftRotate(cls, node):

        y = node
        x = y.right
        t2 = x.left

        x.left = y
        y.right = t2

        y.height = 1 + max(BST.height(y.left), BST.height(y.right))
        x.height = 1 + max(BST.height(x.left), BST.height(x.right))


        return x

    @classmethod
    def rightRotate(cls, node):

        x = node
        y = x.left
        t2 = y.right

        y.right = x
        x.left = t2

        x.height = 1 + max(BST.height(x.left), BST.height(x.right))
        y.height = 1 + max(BST.height(y.left), BST.height(y.right))

        return y

    @classmethod
    def avl(cls, node):

        if (BST.height(node.left) - BST.height(node.right)) > 1:
            if (BST.height(node.left.left) - BST.height(node.left.right)) < 0:
                node.left = BST.leftRotate(node.left)
            node = BST.rightRotate(node)

        if (BST.height(node.left) - BST.height(node.right)) < -1:
            if (BST.height(node.right.left) - BST.height(node.right.right)) > 0:
                node.right = BST.rightRotate(node.right)
            node = BST.leftRotate(node)

        return node



tree = BST()

for item in range(1000000):
    tree.insert(item)


print(tree.root.height)



# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    acc = 0

    def bstToGst(self, root):
        Solution.acc = 0

        self.__revinorder(root)

        return root

    def __revinorder(self, node):
        if not node:
            return

        self.__revinorder(node.right)

        Solution.acc += node.val

        node.val = Solution.acc

        self.__revinorder(node.left)

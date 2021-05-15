# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:

        [bst, val, maxVal, maxValTill] = self.maxSumBSTRec(root)
        return maxValTill

    def maxSumBSTRec(self, node):
        if not node:
            return [True, None, 0, 0]

        [leftBST, leftVal, leftMax, leftMaxTill] = self.maxSumBSTRec(node.left)
        [rightBST, rightVal, rightMax, rightMaxTill] = self.maxSumBSTRec(node.right)

        isBST = leftBST and rightBST

        if (leftVal != None) and (leftVal > node.val):
            isBST = False

        if (rightVal != None) and (rightVal < node.val):
            isBST = False

        if not isBST:
            return [False, node.val, max(leftMax, rightMax), max(leftMaxTill, rightMaxTill)]
        else:
            return [True, node.val, (leftMax + rightMax + node.val),
                    max(leftMaxTill, rightMaxTill, (leftMax + rightMax + node.val))]




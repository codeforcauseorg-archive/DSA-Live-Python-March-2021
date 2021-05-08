# https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root, k: int):

        length = 0
        node = root

        while node:
            node = node.next
            length += 1

        minAll = length // k

        cut = length % k

        current = root

        solution = []

        for outer in range(k):

            solution.append(current)

            chunkSize = minAll

            if outer < cut:
                chunkSize += 1

            for i in range(chunkSize):
                future = current.next

                if i == chunkSize - 1:
                    current.next = None

                current = future

        return solution










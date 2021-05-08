# https://leetcode.com/problems/partition-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class LL:

    def __init__(self):

        self.head = None
        self.tail = None

    def insertLastNode(self, node):

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        node.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        lesser = LL()
        greater = LL()

        node = head

        while node:
            future = node.next
            if node.val < x:
                lesser.insertLastNode(node)
            else:
                greater.insertLastNode(node)

            node = future

        if not lesser.head:
            return greater.head
        else:
            lesser.tail.next = greater.head
            return lesser.head





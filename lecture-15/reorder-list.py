# https://leetcode.com/problems/reorder-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class LL:

    def __init__(self):

        self.head = None
        self.size = 0

    def insertFirst(self, value):

        node = ListNode(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def insertLastNode(self, node):

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        node.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:

        reverse = LL()

        node = head

        while node:
            reverse.insertFirst(node.val)
            node = node.next

        size = reverse.size

        result = LL()

        first = head
        second = reverse.head

        turnFirst = True

        while size > 0:

            if turnFirst:
                future = first.next
                result.insertLastNode(first)
                first = future
            else:
                future = second.next
                result.insertLastNode(second)
                second = future

            size -= 1
            turnFirst = not turnFirst





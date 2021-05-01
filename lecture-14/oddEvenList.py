# https://leetcode.com/problems/odd-even-linked-list/

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
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return head

        oddList = LL()
        evenList = LL()

        current = head
        index = 0

        while current:
            future = current.next

            if index % 2 == 0:
                evenList.insertLastNode(current)
            else:
                oddList.insertLastNode(current)

            index += 1
            current = future

        evenList.tail.next = oddList.head

        return evenList.head








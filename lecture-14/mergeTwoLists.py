# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):

        if not l1:
            return l2

        if not l2:
            return l1

        head = None
        tail = None

        while l1 and l2:

            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next

            if head == None:
                head = node
            else:
                tail.next = node

            tail = node

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return head







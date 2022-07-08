# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        curr = None
        carry = 0
        while l1 or l2 or carry == 1:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            s = v1 + v2 + carry
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0

            node = ListNode(s)
            if head is None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head

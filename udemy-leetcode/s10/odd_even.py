# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        odd = head
        even = odd.next
        evenList = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenList

        return head


def printLinkedList(head):
    ll = ""
    while head:
        ll = f"{ll}{head.val} "
        head = head.next
    print(f"Linked list: {ll}")


head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
printLinkedList(head)
head = s.oddEvenList(head)
printLinkedList(head)

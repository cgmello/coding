# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode()
        temp.next = head
        
        first = temp
        second = temp
        
        for i in range(1, n + 2):
            first = first.next
            
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next        
        
        return temp.next

def printLinkedList(head):
    ll = ""
    while head:
        ll = f"{ll}{head.val} "
        head = head.next
    print (f"Linked list: {ll}")

n = 2

head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

head.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

s = Solution()
printLinkedList(head)
head = s.removeNthFromEnd(head, n)
printLinkedList(head)
    

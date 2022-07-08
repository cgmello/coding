# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        curr = ListNode()
        head = curr
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next

        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        i = 0
        j = len(lists) - 1
        last = j

        # merge first and last
        while last > 0:
            if i >= j:
                i = 0
                j = last

            l1 = lists[i]
            l2 = lists[j]

            print(f"i={i}")
            printLinkedList(l1)
            print(f"j={j}")
            printLinkedList(l2)

            l3 = self.mergeTwoLists(l1, l2)

            print(f"l3:")
            printLinkedList(l3)

            lists[i] = l3
            i += 1
            j -= 1
            last -= 1

        return lists[0]

def printLinkedList(head):
    ll = ""
    while head:
        ll = f"{ll}{head.val} "
        head = head.next
    print (f"Linked list: {ll}")

n = 2

head1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(5)
head1.next = n2
n2.next = n3

head2 = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(4)
head2.next = n2
n2.next = n3

head3 = ListNode(2)
n2 = ListNode(6)
head3.next = n2

head4 = ListNode(-1)
n2 = ListNode(5)
n3 = ListNode(11)
head4.next = n2
n2.next = n3

head5 = ListNode(6)
n2 = ListNode(10)
head5.next = n2

lists = [None, head4, None, head5]

s = Solution()
head = s.mergeKLists(lists)
print("Final:")
printLinkedList(head)


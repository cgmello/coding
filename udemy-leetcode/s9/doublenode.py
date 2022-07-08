class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += str(temp.data) + " "
            temp = temp.next
        print(linked_list)

    def createList(self, arr):
        start = self.head
        n = len(arr)

        temp = start
        i = 0

        while i < n:
            newNode = Node(arr[i])
            if i == 0:
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i += 1

        self.head = start

        return start

    def insertNode(self, val, pos):
        target = Node(val)
        if pos == 0:
            target.next = self.head
            self.head = target
            target.prev = self.head
            return

        def getPrev(pos):
            temp = self.head
            i = 0
            while i < pos:
                temp = temp.next
                i += 1
            return temp

        prev = getPrev(pos)
        nextNode = prev.next
        prev.next = target
        target.prev = prev
        target.next = nextNode
        nextNode.prev = target

    def deleteNode(self, key):
        temp = self.head
        if temp is None:
            return
        if temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp.next.data != key:
            temp = temp.next

        target_node = temp.next
        nextNode = target_node.next
        temp.next = nextNode
        nextNode.prev = temp
        target_node.prev = None
        target_node.next = None


linked_list = LinkedList()
linked_list.createList([1, 2, 3, 4, 5, 6])
linked_list.insertNode(7, 2)
linked_list.deleteNode(4)
linked_list.printList()

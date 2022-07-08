class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Solution:

    def isSymmetricTree(self, tree):
        return self.isMirror(tree, tree)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True

        if t1 is None or t2 is None:
            return False

        return t1.data == t2.data and \
            self.isMirror(t1.right, t2.left) and \
            self.isMirror(t1.left, t2.right)

tree = Node(10)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n4 = Node(1)
n5 = Node(2)
n6 = Node(3)
n7 = Node(4)

tree.left = n1
n1.left = n2
n1.right = n3

tree.right = n4
n4.right = n5
n4.left = n6
# n6.left = n7

s = Solution()
print(s.isSymmetricTree(tree))

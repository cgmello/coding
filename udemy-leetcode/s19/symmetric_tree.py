class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Solution:
    def __init__(self):
        self.isSymmetric = True

    def isSymmetricTree(self, node):
        if node is None:
            return True

        self.preorder(node.left, node.right)

        return self.isSymmetric

    def preorder(self, left_node, right_node):
        if not self.isSymmetric or \
            (left_node is None and right_node is None):
            return

        if (left_node is None and right_node is not None) or \
            (left_node is not None and right_node is None) or \
            (left_node.data != right_node.data):
            self.isSymmetric = False
            return

        self.preorder(left_node.left, right_node.left)
        self.preorder(left_node.right, right_node.right)


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
n4.left = n5
n4.right = n6
# n6.left = n7

s = Solution()
print(s.isSymmetricTree(tree))

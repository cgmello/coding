class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree:
    def maxDepth(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


tree = Node(2)
n4 = Node(4)
n7 = Node(7)
n12 = Node(12)
n15 = Node(15)
n18 = Node(18)

tree.left = n4
tree.right = n7
n7.left = n12
n7.right = n15
n15.left = n18

bt = BinaryTree()
print(bt.maxDepth(tree))

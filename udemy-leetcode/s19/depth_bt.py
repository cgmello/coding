class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class BinaryTree:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root):
        if root is None:
            return 0

        self.inorder(root, 1)

        return self.depth

    def inorder(self, node, count):
        if node is not None:
            self.inorder(node.left, count + 1)
            print(f"data={node.data} count={count}")
            self.inorder(node.right, count + 1)
        else:
            count -= 1
            self.depth = max(self.depth, count)

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


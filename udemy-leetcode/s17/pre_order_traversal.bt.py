class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)

preorder(root)

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)

inorder(root)

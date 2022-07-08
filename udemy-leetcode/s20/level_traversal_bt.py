class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class TreeTraversal:
    def levelTraversal(self, root):
        if root is None:
            return

        print(root.val, end=" ")

        self.leverOrder(root.left, root.right)

    def leverOrder(self, n1, n2):
        if n1 is None and n2 is None:
            return

        v1 = str(n1.val) + " " if n1 else ""
        v2 = str(n2.val) + " " if n2 else ""
        print(f"{v1}{v2}", end="")

        if n1 is not None:
            self.leverOrder(n1.left, n1.right)

        if n2 is not None:
            self.leverOrder(n2.left, n2.right)


root = TreeNode(10)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n5 = TreeNode(5)
n7 = TreeNode(7)
n8 = TreeNode(8)
n20 = TreeNode(20)

root.left = n5
root.right = n20
n5.left = n8
n20.left = n3
n20.right = n7
n7.left = n1
n7.right = n2

trav = TreeTraversal()
trav.levelTraversal(root)

from collections import defaultdict


class Node:
    def __init__(self, value, c):
        self.left = None
        self.right = None
        self.value = value
        self.c = c
        self.huffman = ""


class Tree:
    m = defaultdict(str)
    code = defaultdict(str)
    root = None

    def Huffman(self, s):
        for c in s:
            self.m[c] += 1

        letters = list(m)
        letters.sort(reverse=True)

        self.root = Node(0, None)

        for i in range(len(s)):
            c = letters[i]
            node = Node(m[c], c)
            self.insertTree(self.root, node, "")

    def insertTree(self, root, node, cur):
        if node.val > root.val and root.right is None:
            if root.c is not None:
                root.left = Node(root.val, None)
                root.right = node
                root.val = root.val + node.val
            self.updateTree(root)
            return
        elif node.val <= root.val and root.left is None:
            if root.c is not None:
                root.left = Node(root.val, None)
                root.right = node
                root.val = root.val + node.val
            self.updateTree(root)
            return

        if node.val > root.val:
            self.insertTree(root.left, node)
        else:
            self.insertTree(root.right, node)

    def generateHuffman(self, s):
        print(code)
        # a: 010
        # b: 110
        for c in s:
            print(code[c])
            
    def preorder(self, c):
        pass           
                
    def updateTree(self, root):
        # update code inorder
        code[c] = "11111" a
        pass                


phrase = "Uma boa dicção é fundamental para um canto bonito"
s = Tree()

# 010
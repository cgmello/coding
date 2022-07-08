from collections import defaultdict
from heapq import *

"""
    Huffman Node
"""
class Node:
    def __init__(self, frequency=0, letter=None):
        self.left = None
        self.right = None
        self.frequency = frequency
        self.letter = letter

    # used to compare nodes in heapq
    def __lt__(self, node):
        return self.frequency < node.frequency


"""
    Huffman algorithm
    Huffman coding is a lossless data compression algorithm. 
    In this algorithm, a variable-length code is assigned to input different characters. 
    The code length is related to how frequently characters are used. 
    Most frequent characters have the smallest codes and longer codes for least frequent characters.
    There are mainly two parts. 
    First one to create a Huffman tree, and another one to traverse the tree to find codes.
"""
class Huffman:
    def __init__(self):
        self.huffman_codes = {}
        self.m = defaultdict(int)

    def encode(self, phrase):
        if phrase is None:
            return None

        # count frequencies for each letter
        for c in phrase:
            self.m[c] += 1

        # create list of nodes
        nodes = []
        for c in self.m:
            nodes.append(Node(self.m[c], c))

        # convert the nodes in a priority heap queue
        heapify(nodes)
        
        # create the tree connecting nodes 
        # until there is only one... (the root) - Highlander ;-D
        while len(nodes) > 1:
            # connect 2 small nodes
            left = heappop(nodes)
            right = heappop(nodes)
            newNode = Node(left.frequency + right.frequency)
            newNode.left = left
            newNode.right = right
            
            # push back to queue
            heappush(nodes, newNode)

        # root node
        root = nodes[0]

        # generate huffman codes
        self.generateCode("", root)

        # encode string using huffman codes
        encoded_string = ""
        for c in phrase:
            encoded_string += self.huffman_codes[c]

        return encoded_string

    def generateCode(self, s, node):
        c = node.letter

        # node is a leaf
        if c is not None:
            if s is None:
                # root
                self.huffman_codes[c] = "0"
            else:
                # attribute code
                self.huffman_codes[c] = s
        else:
            # preorder traversal to generate code
            self.generateCode(s + "1", node.left)
            self.generateCode(s + "0", node.right)

    def decode(self, encoded):
        # invert the huffman table
        inverted = {}
        for letter, code in self.huffman_codes.items():
            inverted[code] = letter

        decoded = ''
        subcode = ''

        # decode each code as huffman is not ambiguos
        for c in encoded:
            subcode += c
            if subcode in inverted:
                decoded += inverted[subcode]
                subcode = ''

        return decoded

    def getCodes(self):
        return self.huffman_codes

    def setCodes(self, codes):
        self.huffman_codes = codes


string = "Uma boa dicção é fundamental para um canto bonito"
huffman = Huffman()
encoded = huffman.encode(string)
codes = huffman.getCodes()

print("Encode")
print(f"Input: {string}")
print(f"Huffman codes: {codes}")
print(f"Output: {encoded}")

huffman = Huffman()
huffman.setCodes(codes)
decoded = huffman.decode(encoded)

print()
print("Decode")
print(f"Input: {encoded}")
print(f"Output: {decoded}")

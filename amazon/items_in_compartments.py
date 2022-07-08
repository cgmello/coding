#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#

# * - item
# | - compartment (pair of pipes)

# |**|*|* => 2 closed compartments (2 items and 1 item)
# startIndices = [1,1]
# endIndices = [5,6]
# indexes (1,5) => |**|* there are 2 items in a compartment
# indexes (1,6) => |**|*| there are 2+1 = 3 items in 2 compartments
# Answer: [2,3]

# *|*|*|
# startIndices = [1]
# endIndices = [6]
# Answer: [2]

def numberOfItems(s, startIndices, endIndices):
    # Write your code here
    def push(s, elem):
        s.append(elem)

    def pop(s):
        if len(s) == 0:
            return None

        value = s[len(q)-1]
        del s[len(s)-1]
        return value

    def capacity(s):
        return len(s)

    def solution(s):
        print(s)

        stack = []

        total = 0
        for c in s:
            if c == "|":
                # opening or closing compartment
                while capacity(stack) > 0:
                    v = pop(stack)
                    if v == "*":
                        total += 1
                push(stack, "|")
            elif c == "*":
                if capacity(stack) > 0:
                    push(stack, "*")

        return total

    ans = []
    for i in range(len(startIndices)):
        start = startIndices[i]
        end = endIndices[i]
        total = solution(s[start-1:end])
        ans.append(total)

    return ans

if __name__ == '__main__':
    # s = "*|*|"
    s = "|**|*|*"
    startIndices = [1,1]
    endIndices = [5,6]
    r = numberOfItems(s, startIndices, endIndices)
    print('solution', r)

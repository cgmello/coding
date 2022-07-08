#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

# 10000
# 01000
# 00100
# 00010
# 00001
# Problem: M[i][j] == 1, then j received a gift from i
# If (i,j)=1, then i and j are of the same group (of friends)
# If (i,j)=1 and (j,k)=1, then i, j and k are at the same group
# Answer: number of groups

def countGroups(related):
    # Write your code here
    def get_subgroup(groups, x):
        for subgroup in groups:
            if x in subgroup:
                return subgroup
        return None

    n = len(related)
    g = []

    for i in range(n):
        g.append([i])

    for i in range(n):
        for j in range(n):
            if i != j and related[i][j] == '1':
                # print(i, j, g, related[i][j])

                if [i] in g:
                    g.remove([i])
                if [j] in g:
                    g.remove([j])

                subgroup_i = get_subgroup(g, i)
                subgroup_j = get_subgroup(g, j)
                if subgroup_i is None and subgroup_j is None:
                    g.append([i, j])
                else:
                    s = subgroup_i if subgroup_i is not None else subgroup_j
                    g.remove(s)
                    if i not in set(s):
                        s.append(i)
                    if j not in set(s):
                        s.append(j)
                    g.append(s)

    print(g)

    return len(g)

if __name__ == '__main__':
    # related = ['10000', '01000', '00100', '00010', '00001']
    related = ['1100', '1100', '0110', '0001']
    result = countGroups(related)
    print(result)

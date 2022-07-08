#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Problem: given an array of numbers, separate in A and B groups
# A and B have no elements in common
# Find A (minimal) that sum(A)>sum(B)
# Choose minimal with highest value
# Answer: elements of A in ascending order
# [3,7,5,6,2] => A=[6,7]

def minimalHeaviestSetA(arr):
    # Write your code here
    print('original', arr)
    arr.sort()
    print('sorted', arr)

    # get all groups of A
    groups = []
    subgroup(arr, groups, [], 0)
    print('groups', groups)

    # total of A + B elements
    total = sum(arr)
    print('total sum', total)

    # create a new list with sum(A) > sum(B)
    valid_arr = []
    for a in groups:
        sum_a = sum(a)
        sum_b = total - sum_a
        if sum_a > sum_b:
            valid_arr.append(a)
            print('A, Sum(A), Sum(B)', a, sum_a, sum_b)

    print('valid groups', valid_arr)

    def create_hash(subgroup):
        s = set(subgroup)
        l = [str(x) for x in s]
        return ":".join(l)

    # remove duplicates
    m = {}
    for a in valid_arr:
        h = create_hash(a)
        if h not in m:
            m[h] = 1
        else:
            print("remove duplicate", a)
            valid_arr.remove(a)

    print('cleaned', valid_arr)

    # group by number of elements
    ans = []
    max_sum = 0
    min_elements = float('inf')
    for a in valid_arr:
        len_a = len(a)
        sum_a = sum(a)
        # found a minimal
        if len_a < min_elements:
            ans = a
            min_elements = len_a
            max_sum = sum_a
        # found a minimal with highest value
        elif len_a == min_elements and sum_a > max_sum:
            ans = a
            max_sum = sum_a

    ans.sort()

    return ans

def subgroup(arr, groups, cur, index):
    if index > len(arr):
        return

    # add to list
    groups.append(cur[:])

    # add new element
    for i in range(index, len(arr)):
        if arr[i] not in cur:
            cur.append(arr[i])
            subgroup(arr, groups, cur, i) # recursion
            cur.pop() # backtracking

if __name__ == '__main__':
    arr = [5, 3, 2, 4, 1, 2]
    r = minimalHeaviestSetA(arr)
    print('solution', r)


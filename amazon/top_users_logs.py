#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

# Transactions: "1 2 50" = sender receipt amount
# Problem: users (sender or receipt) that abuses the system (num of transaction > threshold)
# Answer: list of users in ascending order

def processLogs(logs, threshold):
    # Write your code here
    tx = {}
    for log in logs:
        info = log.split()
        sender = info[0]
        recipient = info[1]

        if sender not in tx:
            tx[sender] = 0
        tx[sender] += 1

        if recipient != sender:
            if recipient not in tx:
                tx[recipient] = 0
            tx[recipient] += 1

    # tx2 = {k:v for k,v in sorted(tx.items(), key=lambda x:x[1])}
    # resp = [k for k,v in sorted(tx.items(), key=lambda x:x[1]) if v >= threshold]

    print(tx)

    resp = []
    for k in tx.keys():
        if tx[k] >= threshold:
            resp.append(k)

    def myFunc(e):
        return int(e)

    resp.sort(key=myFunc)

    return resp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

# logs = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
# threshold = 2
# 1
# 2

# logs = ["9 7 50", "22 7 20", "33 7 50", "22 7 30"]
# threshold = 3
# 7

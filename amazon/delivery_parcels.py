#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY parcels as parameter.
#
def getMinimumDays(parcels):
    # Write your code here
    parcels = [int(x) for x in parcels if int(x) > 0]

    if len(parcels) == 0:
        return 0

    parcels.sort(key=int)

    if parcels[0] == 0 and parcels[-1] == 0:
        return 0

    n = 0
    m = min(parcels)
    print(n, m, parcels)
    while m > 0:
        parcels = [int(x - m) for x in parcels if int(x - m) > 0]
        n += 1
        print(n, m, parcels)
        m = min(parcels) if len(parcels) > 0 else 0

    return n

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # parcels_count = int(input().strip())
    # parcels = []
    # for _ in range(parcels_count):
    #     parcels_item = int(input().strip())
    #     parcels.append(parcels_item)
    # result = getMinimumDays(parcels)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    # parcels = [2, 1, 5, 6, 7]
    parcels = [0] * 1000
    parcels += [1] * 2000
    parcels.append(3000)
    print(getMinimumDays(parcels))

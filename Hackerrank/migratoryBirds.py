#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the migratoryBirds function below.


def migratoryBirds(arr):
    count = collections.Counter(arr)
    mx = mxkey = mxid = -1
    for k, v in count.items():
        if mx < v:
            mx = v
            mxkey = k
        elif mx == v:
            mxkey = min(mxkey, k)

    return mxkey


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

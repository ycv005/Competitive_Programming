#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    c = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            while arr[i] != i+1:
                tmp = arr[arr[i]-1]
                arr[arr[i]-1] = arr[i]
                arr[i] = tmp
                c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

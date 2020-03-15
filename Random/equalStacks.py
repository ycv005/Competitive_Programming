#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def sumList(t):
    s=0
    l=[]
    for i in range(len(t)-1,-1,-1):
        s+=t[i]
        l.append(s)
    return l

def equalStacks(h1, h2, h3):
    # https://www.hackerrank.com/challenges/equal-stacks/problem
    s1,s2,s3=sumList(h1),sumList(h2),sumList(h3)

    if len(h1)==1 or len(h2)==1 or len(h3)==1:
        if h1[-1]==h2[-1] and h3[-1]==h2[-1]:
            return h1[-1]
        else:
            return 0
    elif s1[-1]==s2[-1] and s1[-1]==s3[-1]:
        return s1[-1]
    else:
        while (s1[-1]!=s2[-1] or s1[-1]!=s3[-1]):
            if s1[-1]<s2[-1] or s3[-1]<s2[-1]:
                s2.pop()
            elif s1[-1]<s3[-1] or s2[-1]<s3[-1]:
                s3.pop()
            elif s2[-1]<s1[-1] or s3[-1]<s1[-1]:
                s1.pop()
            if len(s1)==0 or len(s2)==0 or len(s3)==0:
                return 0
        return s1[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

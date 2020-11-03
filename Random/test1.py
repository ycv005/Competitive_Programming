import math
import collections
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = "NO"
    if len(arr) == 1:
        res = "YES"
    elif len(arr) == 2 and arr[0] == arr[-1]:
        res = "YES"
    else:
        count = collections.Counter(arr)
        if len(count) == 2:
            v1, v2 = count.values()
            if len(arr) % 2 != 0:
                if abs(v1-v2) % 2 != 0 or v1 == 1 or v2 == 1:
                    res = "YES"
            else:
                # len is even
                val = len(arr)
                if v1 % 2 != 0 or v2 % 2 != 0:
                    # odd + odd
                    res = "NO"
                else:
                    # even + even
                    res = "YES"
        elif len(count) == 1:
            res = "YES"
    print(res)

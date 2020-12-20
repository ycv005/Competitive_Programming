import math


def isPS(x):
    ps = math.sqrt(x)
    return ((ps - math.floor(ps)) == 0)


def lessWithAnyPS(lastPerfectSq, i, dp):
    mn = float('inf')
    for j in range(len(lastPerfectSq)-1, -1, -1):
        lPs = lastPerfectSq[j]
        mn = min(mn, dp[i - lPs])

    return mn


def leastPerfectSqSum(n):
    dp = [0]*(n + 1)
    dp[0] = dp[1] = 1
    lastPerfectSq = [1]
    for i in range(2, n+1):
        if isPS(i):
            lastPerfectSq.append(i)
            dp[i] = 1
        else:
            # dp[i - lastPerfectSq]
            dp[i] = 1 + lessWithAnyPS(lastPerfectSq, i, dp)
    # print(dp)
    return dp[-1]


n = int(input())
print(leastPerfectSqSum(n))

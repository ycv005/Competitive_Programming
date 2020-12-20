def StonesRiverJump(n):
    dp = [0]*(n + 1)
    dp[0] = dp[1] = 1
    dp[2] = 2
    ways = [1, 2]
    for i in range(3, n+1):
        for w in ways:
            dp[i] += dp[i - w]
    # print(dp)
    return dp[-1]


n = int(input())
print(StonesRiverJump(n))

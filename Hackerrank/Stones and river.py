# step - 3- Function is defined to solve probelm
def StonesRiverJump(n):
    # creating dp
    dp = [0]*(n + 1)
    dp[0] = dp[1] = 1
    dp[2] = 2
    # jump ko meine, ways mein store kr liya
    ways = [1, 2]
    # dp 0, 1, 2 jumps ka pata hai, toh 3rd se start kr rahe, n tak
    for i in range(3, n+1):
        for w in ways:
            dp[i] += dp[i - w]
    # print(dp)
    return dp[len(dp)-1]


# step-1- taking input
n = int(input())
# step-2- calling function, when

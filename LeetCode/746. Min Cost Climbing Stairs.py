def minCostClimb(cost,dp,i):
    if i<=1:
        return 0
    elif dp[i]!=-1:
        return dp[i]
    t1 = cost[i-1]+minCostClimb(cost,dp,i-1)
    t2 = cost[i-2]+minCostClimb(cost,dp,i-2)
    dp[i] = t1 if t1<t2 else t2
    return dp[i]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*(len(cost)+1)
        return minCostClimb(cost,dp,len(cost))

# above- top down approach
# below - bottom up approach

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*(len(cost))
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i]+ min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-2] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i-c] + 1)

        return -1 if dp[amount] == -1 else dp[amount]

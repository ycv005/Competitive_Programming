class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sm = sum(nums)
        if S > sm:
            return 0
        target = (sm-S)
        if target % 2 == 0:
            cntZero = 0
            dp = [[0 for j in range((target//2) + 1)]
                  for i in range(len(nums) + 1)]
            for i in range(len(nums) + 1):
                if i < len(nums) and nums[i] == 0:
                    cntZero += 1
                for j in range((target // 2) + 1):
                    if j == 0:
                        dp[i][j] = 1
                        continue
                    elif i == 0:
                        dp[i][j] = 0
                        continue
                    if nums[i-1] == 0:
                        dp[i][j] = dp[i-1][j]
                    elif nums[i-1] <= j:
                        dp[i][j] = dp[i-1][j - nums[i-1]] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
            # print(dp)
            return 2**cntZero * dp[len(nums)][(target//2)]
        else:
            return 0

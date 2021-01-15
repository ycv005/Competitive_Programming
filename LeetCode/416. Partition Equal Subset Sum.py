class Solution:
    def subSetSum(self, nums, n, t, dp):
        if t == 0:
            return True
        elif n == 0 and t > 0:
            return False

        if nums[n-1] <= t:
            return self.subSetSum(nums, n - 1, t - nums[n-1], dp) or self.subSetSum(nums, n-1, t)
        else:
            return self.subSetSum(nums, n-1, t)

    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 == 0:
            dp = [[-1 for j in range(sm//2 + 1)]
                  for i in range(len(nums)+1)]

            # return self.subSetSum(nums, len(nums), sm//2, dp)
            n = len(nums)
            sm = sm//2
            for i in range(len(nums) + 1):
                for j in range(sm + 1):
                    if j == 0:
                        dp[i][j] = True
                        continue
                    elif i == 0:
                        dp[i][j] = False
                        continue

                    if nums[i-1] <= j:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
            return dp[n][sm]
        return False

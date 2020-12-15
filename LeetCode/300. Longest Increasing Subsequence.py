class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            mx = -1
            for j in range(i):
                if nums[j] < nums[i]:
                    mx = max(mx, dp[i])
            if mx > 0:
                dp[i] = mx + 1
        print(dp)
        mx = -1
        for i in range(len(dp)):
            mx = max(mx, dp[i])

        return mx

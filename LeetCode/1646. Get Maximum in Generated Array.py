class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        mx = float('-inf')
        if n <= 1:
            return n
        nums = [0]*(n+1)
        for i in range(1, n+1, 2):
            if i*2 < len(nums):
                nums[i*2] = nums[i]
                mx = max(mx, nums[i], nums[2*i])
            if 2*i + 1 < len(nums):
                nums[(2*i)+1] = nums[i]+nums[i+1]
                mx = max(mx, nums[i], nums[(2*i)+1])
        return mx

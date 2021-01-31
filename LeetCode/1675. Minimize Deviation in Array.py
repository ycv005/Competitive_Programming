# Approach
# To get min difference among numbers, all number should be same, if they are in large categories, by default difference is going to be high

# will be using heap to take out max val, if even, then divide by 2 and store them back. if value popped out is turn out to be odd, then you got a answer by max (which is odd) - smallest.

import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        mn = float("inf")

        for i, v in enumerate(nums):
            if v % 2 != 0:
                nums[i] *= 2

            mn = min(nums[i], mn)
            nums[i] = -1 * nums[i]

        heapq.heapify(nums)
        ans = float('inf')
        while (-1 * nums[0]) % 2 == 0:
            mx = -1 * heapq.heappop(nums)
            ans = min(ans, mx - mn)
            mn = min(mn, mx//2)
            heapq.heappush(nums, -1 * mx//2)

        mx = -1 * heapq.heappop(nums)
        ans = min(ans, mx - mn)

        return ans

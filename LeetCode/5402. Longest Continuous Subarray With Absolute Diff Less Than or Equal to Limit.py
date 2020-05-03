# coding style- PEP8 (standard python)


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        # left and right index for tracing out current subarray
        l = 0
        r = 1
        # number out of this may only create problem
        cur_mx = nums[0]
        cur_mn = nums[0]
        # atleast max_l = 1, bcoz [8] = 8-8 = 0 <= limit
        max_l = 1
        # since, it is like sliding window ques,
        # use while loop with left, right index
        while l <= r and r < len(nums):
            cur_mx = max(cur_mx, nums[r])
            cur_mn = min(cur_mn, nums[r])

            if cur_mx - cur_mn <= limit:
                max_l = max(max_l, r - l + 1)
            else:
                if nums[l] == cur_mx:
                    # need to update cur_mx
                    cur_mx = max(nums[l + 1:r + 1])  # inclusive r
                # using if & not elif bcoz- nums[l] == cur_mn == cur_mx
                if nums[l] == cur_mn:
                    # need to update cur_mn
                    cur_mn = min(nums[l + 1:r + 1])
                l += 1
            r += 1
        return max_l

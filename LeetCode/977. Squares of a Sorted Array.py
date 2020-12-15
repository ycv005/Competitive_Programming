class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            ltsq = nums[l] * nums[l]
            rtsq = nums[r] * nums[r]
            if ltsq > rtsq:
                res = [ltsq] + res
                l += 1
            else:
                res = [rtsq] + res
                r -= 1
        return res

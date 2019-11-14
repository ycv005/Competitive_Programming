# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l!=0:
            k = k%l
        nums[:] = nums[l-k:] + nums[:l-k] # works
        # nums = nums[l-k:] + nums[:l-k] # don't works, don't why

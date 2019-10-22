class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i, val in enumerate(nums):
            t = target-val
            if t not in d:
                d[val]=i
            else:
                return [d[t],i]

# https://leetcode.com/problems/two-sum/
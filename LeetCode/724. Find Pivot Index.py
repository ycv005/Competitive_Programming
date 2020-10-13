class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm = sum(nums)
        ls = 0
        rs = 0
        for i in range(len(nums)):
            tmp = sm - nums[i]
            if i-1>=0:
                ls += nums[i-1]
            rs = tmp - ls
            if ls == rs: return i
        return -1
        
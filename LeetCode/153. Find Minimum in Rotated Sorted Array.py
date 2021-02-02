class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if len(nums) == 1:
            return nums[0]

        while l < r:
            m = (l + r)//2
            if m - 1 >= 0 and nums[m-1] > nums[m]:
                return nums[m]
            # go for that side where array in unbalanced
            # left is sorted, not right
            elif nums[l] <= nums[m] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]

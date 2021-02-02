class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if len(nums) == 1:
            return nums[0]

        while l <= r:
            m = l + (r-l)//2
            if m-1 >= 0 and nums[m-1] > nums[m]:
                return nums[m]

            # look for the unsorted side
            # if left is sorted, right is not
            elif nums[l] <= nums[m] and nums[m] > nums[r]:
                l = m + 1
            # if right is sorted but not left
            elif nums[m] <= nums[r] and nums[l] > nums[r]:
                r = m - 1
            # both side boundary equals to middle element
            # or array is already sorted
            else:
                r -= 1

        return nums[l]

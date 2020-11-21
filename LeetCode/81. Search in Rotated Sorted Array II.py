class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l <= r:
            # let avoid the duplicates
            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r] == [r-1]:
                r -= 1

            m = (l+r)//2

            if nums[m] == target:
                return True

            # let check right of m is sorted or not
            elif nums[m] < nums[r]:
                # target exisiting in range or not
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m-1

            else:
                # if right is not sorted then left should b sorted
                if nums[l] <= target and target < nums[m]:
                    r = m-1
                else:
                    l = m + 1
        return False

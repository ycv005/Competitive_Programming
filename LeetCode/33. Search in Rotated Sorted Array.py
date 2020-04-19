class Solution:
    def search(self, nums, target):
        l,r =0,len(nums)-1
        while l<=r:
            m = (r+l)//2

            if nums[m]==target:
                return m
            elif nums[m]<=nums[r]:  #right-side array is sorted
                # checking for existence of target
                if target>nums[m] and target<=nums[r]:
                    l=m+1
                else: #element won't exist, go to left side array
                    r=m-1
            else: #if right-side is not sorted then left side will be sorted definatively
                # checking for existence of target
                if target>=nums[l] and target<nums[m]:
                    r=m-1
                else: #element won't exist, go to right side
                    l=m+1
        return -1 #didn't find the target

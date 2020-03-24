class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        unSortedEnd = 0
        maxTillNow = float('-inf') #-ve infinity
        for i in range(len(nums)):
            if nums[i]<maxTillNow:
                unSortedEnd = i
            else:
                maxTillNow=nums[i]
        if not unSortedEnd: #array is already sorted
            return 0
        unSortStart = len(nums)-1
        minTillNow = float('inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>minTillNow:
                unSortStart=i
            else:
                minTillNow = nums[i]
        return unSortedEnd - unSortStart + 1

# thanks to https://leetcode.com/patrickf3139 for the Solution

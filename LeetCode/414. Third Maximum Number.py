class Solution:
    def thirdMax(self, nums):
        if len(nums) == 0: return 0
        max1 = nums[0]
        # for ease visualization
        # max3, max2 following max1
        max2 = max3 = None
        for i in range(1, len(nums)):
            # setting up max2, max3
            if nums[i] < max1 and max2 == None:
                max2 = nums[i]
            elif max2 != None and nums[i] < max2 and max3 == None:
                max3 = nums[i]

            if nums[i] > max1:
                # shifting of max, when got a max
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif max2 != None and nums[i] > max2 and nums[i] < max1:
                max3 = max2
                max2 = nums[i]
            elif max3 != None and nums[i] > max3 and nums[i] < max2:
                max3 = nums[i]
        # if anyone not set, return preceding one.
        if max3 == None: return max1
        return max3

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        maxSum = 0
        currSum = 0
        isPos = False
        for i,v in enumerate(nums):
            if currSum + v<0:
                currSum=0
            else:
                isPos = True
                currSum+=v
            maxSum = max(maxSum, currSum)
        return maxSum if isPos else max(nums)

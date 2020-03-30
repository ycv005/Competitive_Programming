class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mx=0
        sm=0
        for i in nums:
            if i==1:
                sm+=1
                mx= sm if sm>mx else mx
            else:
                sm=0
        return mx

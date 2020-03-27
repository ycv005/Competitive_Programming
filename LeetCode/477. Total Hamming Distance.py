class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        s=0
        for i in range(32):
            bitCount=0
            for n in nums:
                bitCount+= (n>>i)&1
            s+=bitCount*(len(nums)-bitCount)
        return s

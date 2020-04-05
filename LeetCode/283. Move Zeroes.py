class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=c=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                c+=1
                i-=1
            i+=1
        nums+=[0]*c

# This one is the required solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prod = 1

        for i in range(len(nums)):
            res[i] *= prod
            prod *= nums[i]
        # till now, each cell is product of previous all number,
        # do same in reverse order
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res


#  below is the faster way-------------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        countZero =0
        for n in nums:
            if n!=0:
                prod*=n
            else:
                countZero+=1
        for i in range(len(nums)):
            if countZero:
                nums[i]= prod if countZero==1 and nums[i]==0 else 0
            else:
                nums[i]=int(prod/nums[i])
        return nums

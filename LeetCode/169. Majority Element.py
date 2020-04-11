class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count =0
        for n in nums:
            if count==0:
                ans=n
            count= count +1 if ans==n else count-1
        return ans

    # boyer-moore voting algo

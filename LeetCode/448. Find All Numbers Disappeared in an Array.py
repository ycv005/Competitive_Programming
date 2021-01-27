class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[nums[i] % len(nums)] += len(nums)
        print(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] / len(nums) <= 1:
                res.append(i)
        return res

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i+1 < len(nums):
            curr = nums[i]
            nxt = nums[i+1]
            if curr == nxt and i+2 < len(nums):
                tmp = nums[i+2]
                if nxt == tmp:
                    nums.pop(i+2)
                    continue
            i += 1
        return len(nums)

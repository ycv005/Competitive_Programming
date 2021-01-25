class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastOnePos = -1

        for i in range(len(nums)):
            v = nums[i]
            if v == 1:
                if lastOnePos == -1:
                    lastOnePos = i
                elif i - lastOnePos <= k:
                    return False
                lastOnePos = i
        return True

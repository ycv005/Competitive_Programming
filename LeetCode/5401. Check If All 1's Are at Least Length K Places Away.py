class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0: return True
        last_pos = None
        for i, n in enumerate(nums):
            if n == 1 and last_pos == None:
                last_pos = i
            elif n == 1:
                if i - last_pos <= k:
                    return False
                else:
                    last_pos = i
        return True

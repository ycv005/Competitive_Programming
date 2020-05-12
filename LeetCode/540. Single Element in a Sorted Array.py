# ------- O(n) Solution------------

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = set()
        for n in nums:
            tmp_len = len(l)
            l.add(n)
            if len(l) == tmp_len:
                return n

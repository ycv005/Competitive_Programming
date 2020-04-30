class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(nums):
            for j, val in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i+j].append(val)
        l = []
        for r in res:
            l+=reversed(r)
        return l

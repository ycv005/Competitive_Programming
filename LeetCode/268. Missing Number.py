def getSumByN(l):
#     Time complexity of len(l) is O(1)
    return (len(l)*(len(l)+1))/2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int(getSumByN(nums))-sum(nums)

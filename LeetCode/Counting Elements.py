import collections
class Solution:
    def countElements(self, arr: List[int]) -> int:
        d= collections.Counter(arr)
        count=0
        for a in arr:
            if a+1 in d:
                count+=1
        return count

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sum(target)==sum(arr)

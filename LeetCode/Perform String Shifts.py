class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for dr,amt in shift:
            if dr==0: #left shift
                s=s[amt:]+s[:amt]
            else: #right shift
                s=s[-amt:] +s[:-amt]
        return s

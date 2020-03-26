class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j=int(c**0.5)
        while j>=0:
            b = (c-j**2)**0.5
            if int(b)==b:
                return True
            j-=1
        return False

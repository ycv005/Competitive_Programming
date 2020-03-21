# since factorial 5 contribute 1 zero, fact 10(5*2) two zero
class Solution:
    def trailingZeroes(self, n: int) -> int:
        s=0
        while n>0:
            n=int(n/5)
            s+=n
        return s

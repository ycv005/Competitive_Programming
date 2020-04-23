import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==n: return m
        if m!=0 and int(math.log(m)/math.log(2))!=int(math.log(n)/math.log(2)):
            # print("perfect sq in present")
            return 0
        elif m==0:
            return 0
        else:
            shift = 0
            # find the common MSB bits.
            while m != n:
                m = m >> 1
                n = n >> 1
                shift += 1
            return m << shift

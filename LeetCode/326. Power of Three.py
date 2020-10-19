import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        v = math.log10(n)/math.log10(3)
        return math.ceil(v) == math.floor(v)

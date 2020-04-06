class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        elif n==1:
            return True
        return n%2==0 and self.isPowerOfTwo(n/2)==True

# not using n&1 to check even/odd bcoz on recursion, if n is float, n&1 won't works

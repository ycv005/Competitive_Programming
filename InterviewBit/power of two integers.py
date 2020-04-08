class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        for p in range(2,33):
            a=round(A**(1/p))
            if(a**p==A):
                return 1
        return 0

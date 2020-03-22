def isOverflow(n):
    if n>(2 ** 31 - 1):
        return 0
    return n

def rev(A):
    if A<0:
        n= -1*isOverflow(int(str(A)[1:][::-1]))
    else:
        n= isOverflow(int(str(A)[::-1]))
    return n

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        return rev(A)

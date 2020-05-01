# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def binarySearch(l, r):
    if l<=r:
        m = (l+r)//2 # 5//2=2, 6//2=3
        currentState = isBadVersion(m)
        if m-1>=1:
            if currentState == True:
                previousState = isBadVersion(m-1)
                if previousState == False:
                    return m
                else:
                    # go to left of array/number
                    return binarySearch(l, m)
            else: # go to right of array/number
                if l == m and m != r:
                    # we are doing so bcoz of // operator
                    # ex - [2,3], m will always 2
                    m = m+1
                return binarySearch(m, r)
        else:
            # only 1 element, so can't check previousState
            if currentState == True:
                return m
            # on border
            elif m==l:
                return binarySearch(l+1, r)
            elif m==r:
                return binarySearch(l, r-1)


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        return binarySearch(1, n)

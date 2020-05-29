from bisect import bisect_right
def getRange(A):
    mn = A[0][0]
    mx = -1
    for i in range(len(A)):
        mn = A[i][0] if A[i][0]<mn else mn
        mx = A[i][-1] if A[i][-1]>mx else mx
    return mn, mx

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        r, c = len(A), len(A[0])
        mn, mx = getRange(A)
        desired_no = (r*c+1)//2
        while mn<mx:
            mid = (mn+mx)//2
            small_count = 0
            for i in range(len(A)):
                small_count += bisect_right(A[i], mid)
            if small_count<desired_no:
                mn = mid + 1
            else:
                mx = mid
        return mn

# https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(h)-1
        mxh = 0
        while l<r:
            tmp = min(h[l],h[r])*abs(r-l)
            if l==0 and r==len(h)-1:
                mxh = tmp
            elif tmp>mxh:
                mxh = tmp
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return mxh
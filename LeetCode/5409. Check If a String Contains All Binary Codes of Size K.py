class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        i=0
        j=k
        mxEnd = 2^k - 1
        isZero = False
        sm = sum(range(0,mxEnd+1))
        while j<len(s):
            tmp = int(s[i:j], 2)
            if tmp >mxEnd:
                return False
            if tmp==0:
                isZero = True
            sm-=tmp
            i+=1
            j+=1
        if sm>0 or not isZero: return False
        return True

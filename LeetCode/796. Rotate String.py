def lps(pat):
    lps = [0]*len(pat)
    j = 0
    i=1
    while i<len(pat):
        if pat[j]==pat[i]:
            j+=1
            lps[i]=j
        elif j>0:
            j = lps[j-1]
            i-=1
        else:
            lps[i]=0
        i+=1
    return lps

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A)!=len(B): return False
        if len(A)==0: return True
        shift = lps(B)
        A = A+A
        i=j=0
        while i<len(A) and j<len(B):
            if A[i]!=B[j] and j>0:
                j=shift[j-1]
                i-=1
            else:
                j+=1
            i+=1
            if j==len(B): return True
        return False

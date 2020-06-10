class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for c in t:
            if c == s[i]:
                i+=1
                if i==len(s)-1:
                    return True
        return False

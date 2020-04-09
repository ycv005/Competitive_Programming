def replaceBack(T):
    j=0
    T=list(T)
    while j>=0 and j<len(T):
        if T[j]=="#":
            if j-1<0:
                T[j]=""
                j-=1
            else:
                T[j-1:j+1]=""
                j-=2
        j+=1

    return "".join(T)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return replaceBack(S)==replaceBack(T)

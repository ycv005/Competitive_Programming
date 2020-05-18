class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n==0 or n==1: return []
        i = 1
        j = 2
        frac = {}
        res = []
        while i<n:
            t = j
            while t<=n:
                if i/j not in frac:
                    frac[i/j] = 1
                    res.append(str(i)+'/'+str(t))
                t+=1
            j +=1
            i+=1
        return res

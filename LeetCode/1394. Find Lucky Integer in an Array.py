class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ln=-1
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if k==v and ln<k:
                ln=v
        return ln

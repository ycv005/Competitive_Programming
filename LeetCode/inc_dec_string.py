class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        tot = len(s)
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        # print(d)
        res=""
        t = sorted(list(set(s)))
        while tot>0:
#             picking shorter
            for j in range(len(t)):
                if d[t[j]]>0: 
                    res+=t[j]
                    tot-=1
                    d[t[j]]-=1
                    if tot==0:
                        break
            for j in range(len(t)-1,-1,-1):
                if d[t[j]]>0: 
                    res+=t[j]
                    tot-=1
                    d[t[j]]-=1
                    if tot==0:
                        break
            # print("res-",res)
        return res
                    
def reduce_s(s,t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            s=s[:i]
            break
    return s

class Solution(object):
    def longestCommonPrefix(self, strs):
        s=""
        if len(strs)==0:
            return s
        s=strs[0]
        for i in range(1,len(strs)):
            if s=="":
                break
            t = strs[i][:len(s)]
            if s != t:
                # sub match
                s=s[:len(t)]
                if s!=t:
                    # iterate from begining to find out commonPart
                    s = reduce_s(s,t)
            else:
                s=s[:len(t)]
        return s

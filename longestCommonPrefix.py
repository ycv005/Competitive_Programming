# https://leetcode.com/problems/longest-common-prefix/submissions/
def reduce_s(strs,s):
    while len(s)>0:
        s=s[:len(s)-1]
        if s in strs[:len(s)]:
            break
    return s

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        if len(strs)==0:
            return s
        prev_f = len(strs[0])
        prev_l = len(strs[-1])
        strs.sort(key= lambda x: len(x))
        suc_f = len(strs[0])
        suc_len = len(strs[-1])
        if prev_l != suc_len or prev_f!=suc_f:
            s = strs[0]
            for i in strs:
                if s not in i[:len(s)]:
                    s = reduce_s(i,s)
        elif len(strs)==1:
            s = strs[0]
        else:
#             all of same length
            s = strs[0]
            for i in range(1,len(strs)):
                if s not in strs[i][:len(s)]:
                    s = reduce_s(strs[i],s)
        return s

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # d={}
        # for i in s:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1
        d = collections.Counter(s)
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1
        # https://leetcode.com/problems/first-unique-character-in-a-string/
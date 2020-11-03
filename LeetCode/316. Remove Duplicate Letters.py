class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 0:
            return ""
        l = [0]*26
        lastIndexVal = 0
        for i, c in enumerate(s):
            num = ord(c) - 97
            if l[num] == 0:
                l[num] = 1
                lastIndexVal = i
            # else leave it.
        res = ""
        for i, v in enumerate(l):
            if v == 1:
                res += str(chr(i+97))
            if i > lastIndexVal:
                break
        return res


"""
t.c = o(n)
space = o(1)
"""

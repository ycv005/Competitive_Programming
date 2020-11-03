class Solution:
    def maxPower(self, s: str) -> int:
        mx = cmx = 1
        prev = s[0]
        for i in range(1, len(s)):
            c = s[i]
            if prev == c:
                cmx += 1
            else:
                cmx = 1
                prev = c
            mx = max(mx, cmx)
        return mx

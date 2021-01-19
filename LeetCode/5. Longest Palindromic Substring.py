class Solution:
    def expandAroundCenter(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return r - l - 1

    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            l1 = self.expandAroundCenter(s, i, i)
            l2 = self.expandAroundCenter(s, i, i+1)

            l = max(l1, l2)
            if l > end - start:
                start = i - (l-1)//2
                end = i + l//2

        return s[start: end+1]

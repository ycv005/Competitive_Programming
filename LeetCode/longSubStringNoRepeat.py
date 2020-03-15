# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ''
        mx = 0
        for c in s:
            if c not in seen:
                seen+=c
            else:
                seen = seen[seen.index(c) + 1:] + c
            mx = max(mx, len(seen))
        return mx
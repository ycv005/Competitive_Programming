class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum(i=='1' for i in s)
        ans = zeros = 0
        # excluding last character, since we have to have a right sub string.
        for c in s[:-1]:
            if c=='0':
                zeros+=1
            else:
                ones-=1
            ans = max(ans, ones + zeros)
        return ans

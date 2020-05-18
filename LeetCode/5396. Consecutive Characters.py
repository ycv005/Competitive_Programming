class Solution:
    def maxPower(self, s: str) -> int:
        if len(s)==0: return 0
        cur_mx = mx  = 1
        elem = s[0]
        for i in range(1, len(s)):
            if s[i] == elem:
                cur_mx +=1
            else:
                cur_mx = 1
                elem = s[i]
            mx = max(mx, cur_mx)
        return mx

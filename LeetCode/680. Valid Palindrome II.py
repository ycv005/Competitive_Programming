class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        mismatch = 0
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                mismatch += 1
                if mismatch > 1:
                    return False
                # remove from left side or remove from right side
                if self.isPalindrome(s, l+1, r) or self.isPalindrome(s, l, r-1):
                    return True
        return True

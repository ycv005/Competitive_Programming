class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        while k > 0 and n > 0:
            if k - n >= 26:
                c = "z"
                k -= 26
            else:
                tmp = 97 + k-n
                c = chr(tmp)
                k -= (tmp - 97 + 1)
            res = c + res
            n -= 1
        return res

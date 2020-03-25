class Solution:
    def longestPrefix(self, s: str) -> str:
        res=""
        for i in range(len(s)-1):
            if s[:i+1]==s[-1*(i+1):]:
                # print("some mathc-",s[:i+1])
                res = s[:i+1]
        return res

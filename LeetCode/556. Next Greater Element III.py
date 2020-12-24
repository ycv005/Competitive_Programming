class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # need to make list, else can't change value
        s = list(str(n))
        changeableIndex = -1
        for i in range(len(s)-2, -1, -1):
            curr = s[i]
            prev = s[i+1]
            if int(prev) > int(curr):
                changeableIndex = i
                break
            else:
                pass
        if changeableIndex == -1:
            return -1
        swapIndex = 0
        for i in range(changeableIndex+1, len(s)):
            if s[changeableIndex] < s[i]:
                swapIndex = i
        s[changeableIndex], s[swapIndex] = s[swapIndex], s[changeableIndex]
        s = s[:changeableIndex+1] + s[changeableIndex+1:][::-1]
        res = int(''.join(s))

        return res if res < 1 << 31 else -1

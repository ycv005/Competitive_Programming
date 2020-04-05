def getDigitSq(n):
    result = 0
    while n:
        x = n % 10
        n = n // 10
        result += x * x
    return result

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = getDigitSq(n)
        while fast!=1 and slow!=fast:
            slow =getDigitSq(slow)
            fast = getDigitSq(getDigitSq(fast))
            if slow==fast: return False
        return True

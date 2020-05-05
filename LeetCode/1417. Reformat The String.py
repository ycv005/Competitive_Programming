def countV(s):
    countA = countN = 0
    for i, c in enumerate(s):
        if ord(c) >= 97:
            countA += 1
        else:
            countN += 1
    return countA, countN

class Solution:
    def reformat(self, s: str) -> str:
        countA, countN = countV(s)
        if abs(countA - countN) > 1: return ''
        # one with more number should start first
        res = ['']*(len(s))
        alphaInd = 1
        digitInd = 0
        if countA > countN:
            alphaInd = 0
            digitInd = 1
        countA = countN = 0
        for i, c in enumerate(s):
            if ord(c)>=97:
                # it is alphabetic character
                if alphaInd < len(s):
                    res[alphaInd] = c
                countA += 1
                alphaInd += 2
            else:
                if digitInd < len(s):
                    res[digitInd] = c
                countN += 1
                digitInd += 2
        return ''.join(res)

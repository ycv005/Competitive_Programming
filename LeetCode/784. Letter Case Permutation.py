def isAlpha(s):
    if (ord(s)>=65 and ord(s)<=90) or (ord(s)>=97 and ord(s)<=122):
        return True
    return False

def getLetter(s, ind, res):
    if ind<len(s):
        # toggle subString on ind
        # if isAlpha(s[ind]):
        if s[ind].isalpha():
            tmp = s[:ind] + s[ind].swapcase() + s[ind+1:]
            res.append(tmp)
            getLetter(tmp, ind+1, res)
        else:
            # digit then don't call func, as below is also doing same
            pass
        # leave it like that, go ahead
        getLetter(s, ind+1, res)

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        getLetter(S, 0, res)
        return res

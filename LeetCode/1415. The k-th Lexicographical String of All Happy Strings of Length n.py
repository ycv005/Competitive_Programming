def createHappyString(s, n, k, str):
    if len(str)>=k: return
    if n==0:
        str.append(s)
    else:
        if s[-1]=='a':
            # keeping order in mind, if a, then add b & then c
            createHappyString(s+'b', n-1, k, str)
            createHappyString(s+'c', n-1, k, str)
        elif s[-1]=='b':
            # keeping order in mind
            createHappyString(s+'a', n-1, k, str)
            createHappyString(s+'c', n-1, k, str)
        elif s[-1]=='c':
            createHappyString(s+'a', n-1, k, str)
            createHappyString(s+'b', n-1, k, str)


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        str = []
        # appending of the string will be lexical
        createHappyString('a', n-1, k, str)
        createHappyString('b', n-1, k, str)
        createHappyString('c', n-1, k, str)
        # print(str)
        if k>len(str): return ""
        return str[k-1]

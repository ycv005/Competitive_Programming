def get_value(a, i, j):
    if i < 0 or j < 0:
        return 0
    try:
        return a[i][j]
    except IndexError:
        return 0


class Solution:
    def __init__(self):
        self.dp = None

    def lcsTabulation(self, s1, s2):
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    self.dp[i][j] = 1 + get_value(self.dp, i-1, j-1)
                else:
                    self.dp[i][j] = max(
                        get_value(self.dp, i-1, j), get_value(self.dp, i, j-1))
        print(self.dp)
        return self.dp[-1][-1]

    def lcsRecursion(self, s1, s2, i, j):
        if i >= len(s1) or j >= len(s2):
            return 0
        if s1[i] == s2[j]:
            self.dp[i][j] = 1 + self.lcs(s1, s2, i+1, j + 1)
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        self.dp[i][j] = max(self.lcs(s1, s2, i+1, j), self.lcs(s1, s2, i, j+1))
        return self.dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # [[ cols ] rows ]
        self.dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]

        # self.lcsRecursion(text1, text2, 0, 0)
        # return self.dp[0][0]
        return self.lcsTabulation(text1, text2)

class Solution:
    def __init__(self, *args, **kwargs):
        self.dp = None

    def minDisRecursive(self, w1, w2, i, j):
        if i >= len(w1):
            return len(w2)-j
        if j >= len(w2):
            return len(w1)-i

        # if already calculated
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if w1[i] == w2[j]:
            # no need to perform any kind of operation
            self.dp[i][j] = 0 + self.minDisRecursive(w1, w2, i+1, j+1)
        else:
            # need to perform any 1 operation
            # replace - i +1, j +1, because we replace 1 char in w1 and go ahead in both
            # delete - i + 1, j - deleting in the word1, to get to word2
            # insert - i, j +1, inserting some value that is related to j, so that's why increaing j
            self.dp[i][j] = 1 + min(self.minDisRecursive(w1, w2, i, j+1),
                                    self.minDisRecursive(w1, w2, i+1, j), self.minDisRecursive(w1, w2, i+1, j+1))
        return self.dp[i][j]

    # def minDisTabulation(self, w1, w2):

    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        self.dp = [[-1 for j in range(len(word2))] for i in range(len(word1))]
        self.minDisRecursive(word1, word2, 0, 0)
        # print(self.dp)
        return self.dp[0][0]

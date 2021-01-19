def factorial(n):
    if n < 0:
        return None
    if n <= 1:
        return 1
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac


class Solution:
    def uniquePathsMemoization(self, m, n, dp):
        if m == 1 or n == 1:
            dp[m][n] = 1
        if dp[m][n] != 0:
            return dp[m][n]
        dp[m][n] = self.uniquePathsMemoization(
            m - 1, n, dp) + self.uniquePathsMemoization(m, n-1, dp)
        return dp[m][n]

    def uniquePathsTabulation(self, m, n, dp):
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 or j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    def uniquePathsCalculate(self, m, n):
        if m == 1 or n == 1:
            return 1
        # becuase we need to go m-1 step down, n- 1 step to right to reach the des, now whatever way we go we need from these moves
        # this is basically the permutation
        m -= 1
        n -= 1
        res = (factorial(m + n))/(factorial(m) * factorial(n))
        return res

    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        # self.uniquePathsMemoization(m, n, dp)
        # self.uniquePathsTabulation(m, n, dp)
        # return dp[m][n]
        return self.uniquePathsCalculate(m, n)

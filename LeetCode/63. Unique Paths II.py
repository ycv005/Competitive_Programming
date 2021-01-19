class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, m):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(
                obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # for i in range(1, m):
        #     if obstacleGrid[i-1][0] == 1:
        #         obstacleGrid[i][0] = 1
        #     elif obstacleGrid[i][0] != 1:
        #         obstacleGrid[i][0] = 0

        # for j in range(1, n):
        #     if obstacleGrid[0][j-1] == 1:
        #         obstacleGrid[0][j] = 1
        #     elif obstacleGrid[0][j] != 1:
        #         obstacleGrid[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + \
                        obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[m-1][n-1]

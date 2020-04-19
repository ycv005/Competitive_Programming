def getMinPath(grid,i,j,dp):
    if i<len(grid) and j<len(grid[0]): #safe to do operation
        if dp[i][j]!=-1: return dp[i][j]
        down = getMinPath(grid,i+1,j,dp)
        right = getMinPath(grid,i,j+1,dp)
        down = down if down!=-2 else right  # have only &  only 1 choice
        right = right if right!=-2 else down # have only &  only 1 choice
        if down==-2 and right==-2: #no choice we have
            down=right=0
        dp[i][j] = grid[i][j] + min(down,right)
        return dp[i][j]
    return -2

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
        return getMinPath(grid,0,0,dp)

# ----------- above is the top-down approach, O(n*m)--------------#

# ----------- generally, bottom-up approach is better only in term of space, & little in performance as no need to take headache of handling recursion

# ----------- below is the bottom-up approach, O(1)-------------#

def isSafe(grid,i,j):
    if i>=0 and j>=0:
        return True
    return False

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                left=up=-2
                if isSafe(grid,r-1,c):
                    up = grid[r-1][c]
                if isSafe(grid,r,c-1):
                    left = grid[r][c-1]
                if left==-2 and up==-2:
                    continue
                left = left if left!=-2 else up
                up = up if up!=-2 else left
                grid[r][c]+= left if left<up else up
        return grid[-1][-1]

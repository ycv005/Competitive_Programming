def doBfs(grid,i,j):
    deq = []
    deq.append([i,j])
    while deq:
        x,y=deq.pop()
        grid[x][y]="v" #visited
        if x+1<len(grid) and grid[x+1][y]=="1":
            deq.append([x+1,y])
        if y+1<len(grid[0]) and grid[x][y+1]=="1":
            deq.append([x,y+1])
        if y-1>=0 and grid[x][y-1]=="1":
            deq.append([x,y-1])
        if x-1>=0 and grid[x-1][y]=="1":
            deq.append([x-1,y])
            
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count= 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    doBfs(grid,i,j)
                    count+=1
        return count
        # https://leetcode.com/problems/number-of-islands/
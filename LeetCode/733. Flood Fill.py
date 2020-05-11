from collections import deque
def dfs(image, sr, sc, newColor):
    val = image[sr][sc]
    image[sr][sc] = newColor
    # up
    if sr-1>=0 and image[sr-1][sc] == val:
        dfs(image, sr-1, sc, newColor)
    # left
    if sc-1>=0 and image[sr][sc-1] == val:
        dfs(image, sr, sc-1, newColor)
    # down
    if sr+1<len(image) and image[sr+1][sc] == val:
        dfs(image, sr+1, sc, newColor)
    # right
    if sc+1<len(image[0]) and image[sr][sc+1] == val:
        dfs(image, sr, sc+1, newColor)
    return image

def isSafeIndex(image, r, c):
    if r<0 or c<0 or r>=len(image) or c>=len(image[0]):
        return False
    return True

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        que = deque([])
        que.append([sr, sc])
        oldColor = image[sr][sc]
        while que:
         curr_r, curr_c = que.popleft()
         image[curr_r][curr_c] = newColor
         for r, c in [[1,0], [0,1], [-1,0], [0,-1]]:
             new_r, new_c = curr_r + r, curr_c + c
             if isSafeIndex(image, new_r, new_c) and image[new_r][new_c] == oldColor:
                 que.append([new_r, new_c])
        return image

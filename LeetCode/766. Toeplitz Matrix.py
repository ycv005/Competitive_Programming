def checkAllSameDiagonal(i,j,matrix):
    nr = len(matrix)
    nc = len(matrix[0])
    while i+1<nr and j+1<nc:
        if matrix[i][j]!=matrix[i+1][j+1]:
            return False
        i+=1
        j+=1
    return True
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        res = True
        for i in range(len(matrix)):
            res = checkAllSameDiagonal(i,0,matrix)
            if res==False:
                break
        if res==True:
            for j in range(1,len(matrix[0])):
                res = checkAllSameDiagonal(0,j,matrix)
                if res==False:
                    break
        return res

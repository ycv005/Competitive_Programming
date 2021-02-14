class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        # easiest way is that, when we think the matrix as a single list
        # 1 way- making list then do binary search- Time- m*n + log(mn) => m*n

        # 2nd way- consider matrix as the virtual flatten list
        # we know that matix[x][y] => matrix[x*m + y]
        # so we can also write it as => matrix[x/m][x%m]
        n, m = len(matrix), len(matrix[0])
        l = 0
        r = n * m - 1
        while l < r:
            mid = (l+r)//2
            v = matrix[mid//m][mid % m]
            if v == target:
                return True
            if v < target:
                l = mid + 1
            else:
                r = mid
        return matrix[l//m][l % m] == target

class Solution:
    def transposeNNMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = self.transposeNNMatrix(matrix)
        # swap col 0 with n-1, then 1 with n-2 and keep going
        # row will remain same
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[0])-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
        return matrix

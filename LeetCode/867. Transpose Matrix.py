class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # all row will be col, and all col be row
        if len(matrix) == len(matrix[0]):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i < j:
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix
        else:
            new_matrix = [[0 for i in range(len(matrix))]
                          for j in range(len(matrix[0]))]
            for i in range(len(matrix[0])):
                for j in range(len(matrix)):
                    tmp = matrix[j][i]
                    new_matrix[i][j] = tmp
            return new_matrix

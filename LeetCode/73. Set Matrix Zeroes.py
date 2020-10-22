class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        for i, mat in enumerate(matrix):
            for j, v in enumerate(mat):
                if v == 0:
                    row.add(i)
                    col.add(j)

        for i, mat in enumerate(matrix):
            r = c = -1
            if i in row:
                row.remove(i)
                r = i
            for j, v in enumerate(mat):
                # don't remove element from col, as this will keep repeat in other
                if r != -1 or j in col:
                    matrix[i][j] = 0

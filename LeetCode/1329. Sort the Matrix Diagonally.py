from collections import defaultdict


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        n, m = len(mat), len(mat[0])

        for i in range(n):
            for j in range(m):
                d[i-j].append(mat[i][j])

        for k in d:
            d[k].sort(reverse=True)

        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i-j].pop()

        return mat

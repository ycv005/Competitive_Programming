class Solution:
    def generate(self, A: int) -> List[List[int]]:
        res = []
        for i in range(A):
            t = [1]*(i+1)
            res.append(t)
        for i in range(1, len(res)):
            for j in range(1, len(res[i])-1):
                t = s = 0
                if j-1 >= 0:
                    t = res[i-1][j-1]
                if j < len(res[i-1]):
                    s = res[i-1][j]
                res[i][j] = s + t
        return res

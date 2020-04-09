class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        res=[]
        for i in range(A):
            t=[1]*(i+1)
            res.append(t)
        for i in range(1,len(res)):
            for j in range(len(res[i])):
                t=s=0
                if j-1>=0:
                    t=res[i-1][j-1]
                if j<len(res[i-1]):
                    s=res[i-1][j]
                res[i][j]= s+ t
        return res

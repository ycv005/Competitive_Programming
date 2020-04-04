def getFibValue(N,mem):
    if mem[N]!=-1: return mem[N]
    mem[N]=getFibValue(N-1,mem) + getFibValue(N-2,mem)
    return mem[N]

class Solution:
    def fib(self, N: int) -> int:
        if N<=1:
            return 1*N
        mem = [-1]*(N+1)
        mem[0]=0
        mem[1]=1
        return getFibValue(N,mem)

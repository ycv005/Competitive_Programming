class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        A.sort()
        mx, mn = A[-1] - K, A[0] + K
        res = A[-1] - A[0]
        for i in range(len(A)-1):
            local_mx = max(mx, A[i] + K)
            local_mn = min(mn, A[i+1] - K)
            res = min(res, local_mx - local_mn)

        return res

def kadaneAlgo(a):
    is_all_neg = True
    ans = cur = None
    min_neg_val = a[0]
    for x in A:
        cur = x + max(cur, 0)
        ans = max(ans, cur)
        if a[i]>0:
            is_all_neg = False
        min_neg_val = max(min_neg_val, a[i])
    if is_all_neg:
        return min_neg_val
    return ans

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A)==0: return 0
        max_kadane = kadaneAlgo(A)
        if max_kadane<=0:
            # all negative or all neg with alteast 1 zero
            return max_kadane
        sm_array = 0
        for i in range(len(A)):
            sm_array += A[i]
            A[i] = -A[i]
        max_kadane2 = sm_array + kadaneAlgo(A)
        return max_kadane if max_kadane > max_kadane2 else max_kadane2

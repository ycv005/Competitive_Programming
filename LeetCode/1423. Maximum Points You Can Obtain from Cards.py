class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        if k==len(cp): return sum(cp)
        mx = sm = sum(cp[:k])

        # assuming first k values are mx from left side
        # now will reduce 1 each time & add 1 from right side,
        # to get maxScore
        ind = k-1
        for i in range(1,k+1):
            sm -= cp[ind] + cp[-i]
            mx = mx if mx>sm else sm
            ind-=1
        return mx

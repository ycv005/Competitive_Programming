class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last_num = 0
        res = 0
        for i, v in enumerate(arr):
            diff = v - last_num - 1
            if diff >= 1:
                if diff >= k:
                    res = last_num + k
                    break
                k -= v - last_num - 1
            last_num = v
        if k > 0:
            res = last_num + k
        return res

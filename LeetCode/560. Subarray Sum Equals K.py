# solving with via the preffix sum

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        sm = 0
        res = 0
        for n in nums:
            sm += n
            res += count.get(sm - k, 0)
            count[sm] = count.get(sm, 0) + 1
        return res

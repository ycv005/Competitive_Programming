class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # solve this with the prefix sum

        target = -x

        for n in nums:
            target += n
        if target == 0:
            return len(nums)

        hsmap = {}
        hsmap[0] = - 1
        res = float('-inf')
        sm = 0

        # till here the target will be=> totalSum- x, this is what we are looking for.
        # so sm - target is => sm - (totalSum - x)
        for i in range(len(nums)):
            sm += nums[i]
            if sm - target in hsmap:
                # store the max size,
                # so the second params is end - start  +1
                res = max(res, i - hsmap[sm - target])

            hsmap[sm] = i

        return -1 if res == float('-inf') else len(nums) - res

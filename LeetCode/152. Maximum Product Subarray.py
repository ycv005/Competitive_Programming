class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final_mx = curr_mx = curr_min = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            tmp = curr_mx
            curr_mx = max(max(curr_mx*n, curr_min*n), n)
            curr_min = min(min(curr_min*n, tmp*n), n)

            final_mx = max(curr_mx, final_mx)
        return final_mx

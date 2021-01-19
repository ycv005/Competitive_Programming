from collections import Counter


class Solution:
    def twoPointer(self, nums, k):
        nums.sort()
        l = 0
        r = len(nums)-1
        count = 0
        while l < r:
            lt = nums[l]
            rt = nums[r]
            if lt + rt == k:
                count += 1
                l += 1
                r -= 1
            elif lt + rt < k:
                l += 1
            else:
                r -= 1
        return count

    def hashMap(self, nums, k):
        count = 0
        freq = Counter(nums)

        for key, v in freq.items():
            if k - key in freq:
                count += min(v, freq[k-key])

        # since counting a pair 2 time
        return count//2

    def maxOperations(self, nums: List[int], k: int) -> int:
        # return self.twoPointer(nums, k)
        return self.hashMap(nums, k)

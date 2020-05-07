class Solution:
    def firstMissingPositive(self, nums):
        # since hashing key must starts from 0
        # need to append 0, in case [1,2,3,4]
        # if we won't add, we can't manipulate 0th index
        # as hash function won't reach there
        nums.append(0)
        N = len(nums)

        # deleting useless values
        for i in range(N):
            if nums[i] < 0 or nums[i]>=N:
                nums[i] = 0
        print(nums)
        # use index as hash to record the element presence status
        for i in range(N):
            nums[nums[i]%N] += N
        print(nums)
        for i in range(N):
            if nums[i]//N == 0:
                return i
        return N

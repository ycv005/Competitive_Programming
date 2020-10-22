class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the minimun number which could be replaced
        replace_index = replace_with_index = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                replace_index = i-1
                break
        if replace_index == -1:
            nums.sort()
        else:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[replace_index]:
                    replace_with_index = i
                    break
            # swap the replace index with replace_with_index
            nums[replace_index], nums[replace_with_index] = nums[replace_with_index], nums[replace_index]

            # now make all number in sorted order or reverse them as reversing will give a sorted order

            if replace_index <= len(nums)-1:
                # print(nums[:replace_index+1], sorted(nums[replace_index+1:]))
                nums[:] = nums[:replace_index+1] + \
                    sorted(nums[replace_index+1:])
            else:
                nums[:] = nums[:replace_index+1]

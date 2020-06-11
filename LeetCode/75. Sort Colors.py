# Idea- Append all 2's to the last of list (2 is sorted in-place order)
# 0's - Insert all 0's to the begining using last seen zero index
# 1's - leave it like it is, it will be sorted automatically
# use a Variable n to count whether operation on all is performed or not, as it can't be done by index as it is being modified

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZeroInd = 0
        i = 0
        n = len(nums)
        while i<len(nums):
            if nums[i] == 2:
                tmp = nums.pop(i)
                nums.append(tmp)
                i -= 1 # need to do this, as element next to 2 will now come at i index after pop
            elif nums[i] == 0:
                tmp = nums.pop(i)
                nums.insert(lastZeroInd, tmp)
                lastZeroInd += 1
                # i -= 1 # not this bcoz once 0 is poped & added to begining, previous elem to 0 will come at i index
            i += 1
            n -= 1
            if n == 0: break

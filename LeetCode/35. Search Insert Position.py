def getPos(nums,l,r,t):
    if l<=r:
        mid = int((l+r)/2)
        if nums[mid]==t:
            return mid
        elif nums[mid]>t: #move left
            return getPos(nums,l,mid-1,t)
        else:
            return getPos(nums,mid+1,r,t)
    else:
#      mean, l>r, since l is greater and at r some element is present
        return l

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return getPos(nums,0,len(nums)-1,target)

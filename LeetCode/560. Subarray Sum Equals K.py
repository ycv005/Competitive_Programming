class Solution:
    def subarraySum(self,nums,k):
        s=i=count=0
        for j in range(len(nums)):
            if nums[j]>k:
                s=0
                i=j+1
            elif nums[j]==k:
                count+=1
                s=0
                i=j+1
            else:
                s+=nums[j]
                if s==k:
                    count+=1
                    s-=nums[i]
                    i+=1
        return count

nums=[3,3,3,3,1,2,2,1,1]
k=2
s = Solution()
print(s.subarraySum(nums,k))

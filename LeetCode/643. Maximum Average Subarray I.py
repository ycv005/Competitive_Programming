from collections import deque
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = deque(nums[:k])
        tmpSum = maxSum =sum(tmp)
        for i in range(k,len(nums)):
            tmpSum = tmpSum - tmp.popleft()+ nums[i]
            tmp.append(nums[i])
            if tmpSum > maxSum: maxSum = tmpSum
        return maxSum/k

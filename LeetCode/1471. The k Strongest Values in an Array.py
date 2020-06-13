# Idea- Strongest value are willing to realy on boundary either side, and then inward with decreasing intesity.
# Steps to solve
# Sort, get median, and assign lastPointer, startPointer
# compare lastPointer's element with startPointer's element, then add accordingly
# only iterate loop for k, because elements in start and last with range of k, have Strongest value

# OR
# Explaination(hindi lang.)- https://www.youtube.com/watch?v=mvbTN2I3HxY

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        lastPointer = -1
        startPointer = 0
        mInd = (len(arr)-1)//2
        m = arr[mInd]
        res = []
        for i in range(k):
            if abs(arr[lastPointer] - m) >= abs(arr[startPointer] - m):
                res.append(arr[lastPointer])
                lastPointer -= 1
            else:
                res.append(arr[startPointer])
                startPointer += 1
        return res

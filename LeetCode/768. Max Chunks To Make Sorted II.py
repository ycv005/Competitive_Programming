class Solution:
    def maxChunksToSorted(self, l: List[int]) -> int:
        sortL = sorted(l)
        sum1=sum2=0
        count=0
        for i in range(len(l)):
            sum1+=l[i]
            sum2+=sortL[i]
            if sum1==sum2:
                # print("got a chunk at-",i)
                count+=1
                sum1=sum2=0
        return count

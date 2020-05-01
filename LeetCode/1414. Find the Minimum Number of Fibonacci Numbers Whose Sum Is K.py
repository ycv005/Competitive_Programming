def checkSub(dp, k):
    count = 0
    for i, val in enumerate(dp):
        if val==k:
            k-=val
            count+=1
        elif k%val==0:
            count += k//val
            k=0
        elif val<k:
            k-=val
            count+=1
        if k<=0:
            break
    return count if k==0 else 0

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        dp = [1,1]
        i=2
        # fibonacci in reverse
        while dp[0]<=k: #dp[-1]<=k:
            # dp.append(dp[0]+dp[1])
            dp.insert(0, dp[0]+dp[1])
        # print(dp)
        count = 0
        for i, val in enumerate(dp):
            if val==k:
                return 1
            elif k%val==0:
                count = k//val
                break
            elif val<k:
                status = checkSub(dp[i+1:], k-val)
                if status!=0:
                    count = 1 + status
                    break

        return count

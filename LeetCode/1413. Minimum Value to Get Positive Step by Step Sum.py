class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mn = min(nums)
        if mn>0:
            return mn
        elif mn==0:
            return 1
        # mn is -ve
        startvalue = abs(mn)
        sm = 0
        gotMinVal = False
        while not gotMinVal:
            startvalue+=1
            for n in nums:
                sm+=n
                if sm<1:
                    print("breaking")
                    sm=0
                    break
                elif sm>=1:
                    gotMinVal = True
            # for loop won't break
            # gotMinVal = True
        return startvalue

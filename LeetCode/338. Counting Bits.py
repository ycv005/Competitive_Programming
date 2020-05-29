class Solution:
    def countBits(self, num: int) -> List[int]:
        if num==0: return [0]
        res  = [0]*(num+1)
        for i in range(1,num+1):
            if i&1: # i is odd
                # from even to odd, 1 bit is surely add
                res[i] = res[i-1] + 1
            else: # i is even
                # ex- 5 & 10, both have same 1's bit
                # when 5 is multiply by 2, 0 bit is added to right
                res[i] = res[i//2]
        return res

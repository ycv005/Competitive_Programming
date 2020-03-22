def getFactor(num):
    sm=num+1
    i=2
    j=0
    while i<=(num**0.5):
        if num%i==0:
            if i!=int(num/i):
                sm+=i+int(num/i)
                j+=1
            else:
                sm+=i
            j+=1
            if j>2:
                return 0
        i+=1

    return sm if j==2 else 0


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            s+=getFactor(i)
        return s

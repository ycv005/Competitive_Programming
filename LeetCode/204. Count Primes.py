# to check if number is even-
# not (n & 1)
# for odd
# (n & 1)

def is_prime(n):
    i=2
    while n>2 and i<n**0.5:
        if n%i==0:
            return False
        i+=1
        if not n&1:
            i+=1
    return True

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        isPrimeBool = [1]*(n+1)
        isPrimeBool[0] = isPrimeBool[1] =  0
        count=0
        for i in range(2,n):
            if not isPrimeBool[i]:
                continue
            for j in range(2,int(n/i)+1):
                isPrimeBool[i*j]=0
            if isPrimeBool[i]!=1 and not is_prime(i):
                isPrimeBool[i]=0
        isPrimeBool[2]=1
        for i in range(2,len(isPrimeBool)-1):
            if isPrimeBool[i]==1:
                count+=1
        return count

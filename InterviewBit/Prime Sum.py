def isPrime(n):
    i=2
    while n>2 and i<=n**0.5:
        if n%i==0:
            return False
        i+=1
    return True

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        a=2 #need to find b
        if isPrime(A-a):
            return [a,A-a]
        a+=1
        while a<=int(A/2):
            if isPrime(a) and isPrime(A-a):
                return [a,A-a]
            a+=2 #only checking on odd number as they will only be prime

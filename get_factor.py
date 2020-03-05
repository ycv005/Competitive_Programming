import math
def get_factors(n):
    i=2
    fac = []
    while i<=math.sqrt(n):
        if n%i==0:
            fac.append([i,int(n/i)])
        i+=1
    return fac

# n=int(input())
n=100
print(get_factors(n))
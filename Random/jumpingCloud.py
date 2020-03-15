# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

n = int(input())
c = [int(i) for i in input().split()]
if len(c)==2:
    return 1
else:
    i=0
    j=0
    while(i<len(c)-1):
        if i+2<len(c) and c[i+2]==0:
            i+=2
        else:
            i+=1
        j+=1
    return j
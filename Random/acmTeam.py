# https://www.hackerrank.com/challenges/acm-icpc-team/problem

from itertools import combinations

n,m=[int(i) for i in input().split()]
d = {}
l=[]
for i in range(n):
    t=[]
    s = input()
    for i in range(len(s)):
        if int(s[i])==1:
            t.append(i+1)
    l.append(t)
    
comb = list(combinations(l, 2))
# print(comb)
m=0
for i in comb:
    a = len(set(i[0]+i[1]))
    if a in d:
        d[a]+=1
    else:
        d[a]=1
    if a>m:
        m=a
print(m)
print(d[m])
# return 


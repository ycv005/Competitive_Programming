#https://www.hackerrank.com/challenges/missing-numbers/problem

n=int(input())
arr = [int(i) for i in input().split()]
m=int(input())
brr = [int(i) for i in input().split()]
d={}
# f=[]
for i in brr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
# print(d)
for i in arr:
    if i in d:
        d[i]-=1
        if d[i]==0:
            del d[i]
# print(d)
t = list(d.keys())
t.sort()
# return t
print(t)

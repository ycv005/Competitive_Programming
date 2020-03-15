# https://www.codechef.com/MARCH20B/problems/CHPINTU
for t in range(int(input())):
    n,m = map(int,input().split())
    f = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    d={}
    mn= 100000000
    for i in range(n):
        if f[i] not in d:
            d[f[i]]=p[i]
        else:
            d[f[i]]+=p[i]
    # print(d)
    for i,v in d.items():
        if v<mn:
            mn = v
    print(mn)
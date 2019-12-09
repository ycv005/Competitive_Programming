# https://www.codechef.com/DEC19B/problems/WATSCORE

for t in range(int(input())):
    n = int(input())
    d={}
    for _ in range(n):
        i,v = map(int,input().split())
        if i<9:
            if i in d:
                if d[i]<v:
                    d[i]=v
            else:
                d[i]=v
    s=0
    for i in d.keys():
        s+=d[i]
    print(s)

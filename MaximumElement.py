n = int(input())
l=[]
m=0
for i in range(n):
    s = input()
    if s[0]=="1":
        t,val = s.split(" ")
        # m.append(int(val))
        l.append(int(val))
        # heapq.heapify(m)
        if m<int(val):
            m = int(val)
    elif s[0]=="2":
        if len(l)!=0:
            if m==l.pop():
                if len(l)!=0:
                    m = max(l)
                else:
                    m=0
    else:
        print(m)

# https://www.hackerrank.com/challenges/maximum-element/problem

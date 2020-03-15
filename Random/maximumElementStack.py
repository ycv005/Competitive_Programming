n = int(input())
l=[]
m=[]
for i in range(n):
    s = input()
    if s[0]=="1":
        t,val = s.split(" ")
        l.append(int(val))
        if len(m)==0:
            m.append(int(val))
        elif m[-1]<=int(val):
            m.append(int(val))
    elif s[0]=="2":
        if len(l)!=0:
            tmp = l.pop()
            if len(m)!=0 and tmp==m[-1]:
                m.pop()
    else:
        print(m[-1])

# https://www.hackerrank.com/challenges/maximum-element/problem
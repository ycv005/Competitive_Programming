# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def bSearch(l,s,e,v):#l is in reverse order
    if e>=s:
        mid = s+int((e-s)/2)
        if l[mid]==v:
            return mid
        elif l[mid]>v:
            # looking into right sub array
            return bSearch(l,mid+1,e,v)
        elif v>l[mid]:
            # left sub array
            return bSearch(l,s,mid-1,v)
    else:
        if l[s]<v:
            return s
        else:
            return s+1


n = int(input())
scr=[]
s = input().split()
for i in range(len(s)):
    if i!=0:
        if s[i]!=s[i-1]:
            scr.append(int(s[i]))
    else:
        scr.append(int(s[i]))

m = int(input())
ascr = [int(i) for i in input().split()]
pos = []
p=0
for i in range(m):
    if ascr[i]<scr[-1]:
        pos.append(len(scr))
    elif ascr[i]==scr[-1]:
        pos.append(len(scr)-1)
    elif ascr[i]>=scr[0]:
        pos.append(0)
    elif i-1>=0 and ascr[i]==ascr[i-1]:
        pos.append(pos[-1])
    else:
        if len(pos)!=0:
            p= bSearch(scr,0,pos[-1]-1,ascr[i])
        else:
            p= bSearch(scr,0,len(scr)-1,ascr[i])
        pos.append(p)

    
for i in pos:
    print(i+1)
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

n,m = input().split()
a={}
b={}
for i in input().split(" "):
    if i in a:
        a[i]+=1
    else:
        a[i]=1

flag=1
for i in input().split(" "):
    if i in a:
        a[i]-=1
        print(a)
        if a[i]==0:
            a.pop(i)
            
    else:
        flag=0
        break

if flag==0:
    print("No")
else:
    print("Yes")

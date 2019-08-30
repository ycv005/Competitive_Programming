n,m = [int(i) for i in input().split(" ")]
l = [0 for i in range(n)]
ma,t= 0,0 
for i in range(m):
    a,b,k = input().split(" ")
    l[int(a)-1]+= int(k)
    if int(b) <n:
        l[int(b)] -=int(k)

for i in range(n):
    t+=l[i]
    if ma<t:
        ma = t

# print(l)
print(ma)
# https://www.hackerrank.com/challenges/crush/problem
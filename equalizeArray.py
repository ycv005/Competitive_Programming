# https://www.hackerrank.com/challenges/equality-in-a-array/problem

n = int(input())
a = input()
d = {}
m=0
for i in a:
    if i!=' ':
        if int(i) in d:
            d[int(i)]+=1
        else:
            d[int(i)]=1
        if d[int(i)]>m:
            m = d[int(i)]
print(n-m)

    
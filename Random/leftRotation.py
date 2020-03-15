n,d = [int(i) for i in input().split(" ")]
l = [int(i) for i in input().split(" ")]
a=l[:]
for i in range(n):
    l[(n-d + i)%n] = a[i]

for j in l:
    print(j, end=" ")
# https://www.hackerrank.com/domains/data-structures/arrays
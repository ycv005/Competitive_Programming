l = [0]*(1000001)
l[1] = 1
i = 2
while i<len(l):
    l[i] = i + l[i-1] + i*l[i-1]
    l[i] = l[i]%1000000007
    i+=1

for t in range(int(input())):
    n = int(input())
    print(l[n])

# https://www.codechef.com/problems/REDONE
# thinking approach, why did this worked and how you thought
# why array used- since for each test case, we where looking onto same result,
# only difference was range. That is overlapping problems

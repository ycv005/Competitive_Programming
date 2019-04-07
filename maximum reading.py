n = int(input())
l = list(map(int,input().split()))
high = []
count=0
dup=l[:]
mxval = max(l)
dup=list(filter(lambda a: a != mxval, dup))
for i in range(len(l)):
    if l[-1]==l[i]:
        count+=1

dup.sort()
# print(dup)
if count!=len(l):
    high.append(dup[-1])
    for i in range(len(l)):
        if high[0]<(l[-1]%l[i]):
            high.append(l[-1]%l[i])
else:
    high.append(0)

print(max(high))
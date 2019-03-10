#//https://www.codechef.com/JAN19B/problems/DPAIRS
n,m=input().split()
n,m=int(n),int(m)
a= list(map(int,input().split()))
b= list(map(int,input().split()))
dic={}
# for i in range(len(a)):
#     for j in range(len(b)):
#         dic[a[i]+b[j]]=[i,j]


    
mina=a.index(min(a))
maxb=b.index(max(b))
if mina==maxb:
        maxb=b.index(min(b))

j=0
while (j<len(b) or j<len(a)):
        if j<len(b):
                dic[a[mina]+b[j]]=[mina,j]
        if j<len(a):
                dic[b[maxb]+a[j]]=[j,maxb]
        j+=1
j=0
print(dic)
for v in dic.values():
        if j<n+m-1:
                print(v[0],v[1])
        else:
                break
        j+=1
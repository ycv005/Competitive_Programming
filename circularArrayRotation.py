#https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
    l=a[:]
    n=len(a)
    if n!=1:
        k%=n
        if k!=0:
            for i in range(len(a)):
                l[(i+k)%n]=a[i]
    t=[]
    for q in queries:
        t.append(l[q])
    # print("new-",l)
    return t

nkq = input().split()

n = int(nkq[0])

k = int(nkq[1])

q = int(nkq[2])

a = list(map(int, input().rstrip().split()))

queries = []

for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)

result = circularArrayRotation(a, k, queries)
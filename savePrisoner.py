# https://www.hackerrank.com/challenges/save-the-prisoner/problem
def saveThePrisoner(n, m, s):
    if n==1:
        return s
    if m>n:
        m=m%n
    res = s if m==1 else (m+s-1)%n
    return n if res==0 else res

t = int(input())

for t_itr in range(t):
    nms = input().split()

    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])
    result = saveThePrisoner(n, m, s)
    print(result)
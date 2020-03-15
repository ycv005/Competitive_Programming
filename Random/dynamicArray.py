n,q= [int(i) for i in input().split(" ")]
# print(n,q)
sql = [[] for i in range(n)]
la = 0
for q1 in range(q):
    l= [int(i) for i in input().split(" ")]
    if l[0] == 1:
        ind =  ((l[1] ^ la)%n)
        sql[ind].append(l[2])
    else:
        ind =  ((l[1] ^ la)%n)
        la = sql[ind][l[2]%len(sql[ind])]
        print(la)
# https://www.hackerrank.com/challenges/dynamic-array/problem
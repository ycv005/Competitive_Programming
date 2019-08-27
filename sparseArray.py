n = int(input())
s = []
for i in range(n):
    s.append(input())
nq = int(input())
res = [0 for i in range(nq)]
for i in range(nq):
    # q = input()
    # res[i] = s.count(q)
    print(s.count(input()))
# https://www.hackerrank.com/challenges/sparse-arrays/problem
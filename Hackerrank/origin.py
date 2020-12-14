from collections import Counter

n, m = map(int, input().split())
x = input()
y = input()
xd = Counter(x)

res = "YES"

for c in y:
    if c not in xd:
        res = "NO"
        break
    else:
        xd[c] -= 1
        if xd[c] == 0:
            del xd[c]
print(res)

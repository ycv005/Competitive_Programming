s = input()
q = int(input())
isReverse = False
for _ in range(q):
    query = input()
    if len(query) > 1:
        t, f, c = query.split()
        f = int(f)
        if isReverse:
            if f == 1:
                f = 2
            else:
                f = 1
        if f == 1:
            s = c + s
        else:
            s += c
    else:
        isReverse = not isReverse

if isReverse:
    s = s[::-1]
print(s)

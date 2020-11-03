import math
n, m, p = list(map(int, input().split()))
mat = []
col_prod = [1]*m
count = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    if math.prod(tmp) % p == 0:
        count += 1
    for j, v in enumerate(tmp):
        col_prod[j] *= v
    mat.append(tmp)

    for j, v in enumerate(col_prod):
        if v % p == 0:
            count += 1
# print(mat)
# only check dia prod

dia_prod = []

if math.prod([v[i] for i, v in enumerate(mat)]) % p == 0:
    count += 1

if math.prod([v[~i] for i, v in enumerate(mat)]) % p == 0:
    count += 1

print(count)

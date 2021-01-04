n, k = map(int, input().split())
l = list(map(int, input().split()))
res = [""]*k
if n <= k:
    for i, c in enumerate(l):
        res[i] = c
    while n < k:
        res[n] = None
        n += 1
else:
    # first get the number for dividing
    div = []
    while n > 0 and k > 0:
        tmp = n // k
        div.insert(0, tmp)
        n -= tmp
        k -= 1
    if n > 0:
        div.insert(0, n)
    print(div)

    last = 0
    l = list(map(str, l))
    print("orogi- ", l)
    for i, r in enumerate(div):
        print(last, r)
        res[i] = " ".join(l[last:last+r])
        last += r


print(res)
for i, v in enumerate(res):
    if v == None:
        print("null")
    else:
        print(v)

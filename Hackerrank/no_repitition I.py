s = input()
l = r = 0
st = {}
mx = cmx = lt = rt = 0

while r < len(s):
    c = s[r]
    if c not in st:
        st[c] = r
        # cmx += 1
    else:
        # save if max
        if r-l > rt - lt:
            lt = l
            rt = r - 1
            # mx = max(mx, cmx)
        l = st[c] + 1
        r = l
        st = {}
        st[s[r]] = r
        # cmx = 1
    r += 1

if r-l > rt-lt:
    lt = l
    rt = r - 1

res = s[lt:rt+1]
res_len = rt-lt+1
# if res[0] == res[-1] and len(res) > 1:
#     res = res[1:]
#     res_len -= 1

print(res_len)
print(res)

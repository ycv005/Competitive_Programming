for t in range(int(input())):
    n, m = map(int, input().split())
    ln = list(map(int, input().split()))
    lm = list(map(int, input().split()))
    ln.sort()
    lm.sort(reverse=True)
    # print(ln)
    # print(lm)
    sum_n = sum(ln)
    sum_m = sum(lm)
    swap = -1
    if sum_n > sum_m:
        swap = 0
    else:
        swap = 0
        for i in range(n):
            if i == m:
                # reached to the end of m
                if sum_n <= sum_m:
                    swap = -1
                break
            ni = ln[i]
            mi = lm[i]
            sum_n += mi - ni
            sum_m += ni - mi
            swap += 1
            if sum_n > sum_m:
                break
    if sum_n <= sum_m:
        swap = -1
    print(swap)

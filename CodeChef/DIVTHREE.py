for t in range(int(input())):
    n, k, d = map(int, input().split())
    total_q = sum(list(map(int, input().split())))
    # for i in range(n):
    #     total_q += int(input())

    next_d = total_q // k

    if next_d > d:
        next_d = d
    print(next_d)

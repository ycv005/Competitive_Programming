for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    sm = sum(l)
    if sm % k == 0:
        print(0)
    else:
        print(1)

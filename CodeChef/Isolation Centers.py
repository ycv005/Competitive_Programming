from collections import Counter
for t in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    d = Counter(s)
    for _ in range(q):
        c = int(input())
        que = 0
        for k, v in d.items():
            if c<v:
                que += v-c
        print(que)

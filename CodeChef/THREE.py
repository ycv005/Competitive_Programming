from collections import Counter

for _ in range(int(input())):
    s = input()
    freq = Counter(s)
    sm = 0
    for k, v in freq.items():
        sm += v//2
    print(min(sm, len(s)//3))

n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
seen = set()
cm = 0
for a in l1:
    seen.add(a)

for b in l2:
    if b in seen:
        cm = b
        break

print(cm)

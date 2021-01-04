n1, n2, n3 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))

# pop from 0
s1 = sum(l1)
s2 = sum(l2)
s3 = sum(l3)

while s1 != s2 and s2 != s3:
    mnsum = min(s1, min(s2, s3))
    if s1 > mnsum:
        s1 -= l1.pop(0)
    if s2 > mnsum:
        s2 -= l2.pop(0)
    if s3 > mnsum:
        s3 -= l3.pop(0)

    # any of them unable to make upto it
    if len(l1) == 0 or len(l2) == 0 or len(l3) == 0:
        s1 = 0
        break

# print any
print(s1)

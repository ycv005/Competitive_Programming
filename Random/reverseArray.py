i = int(input())
l = [int(i) for i in input().split(' ')][::-1]
# print(l)
for i in l:
    print(i, end=" ")
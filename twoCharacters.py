def isAlternate(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return False
    return True

from itertools import combinations
n = int(input())
s = input()
l = []
for i in list(s):
    if len(l) ==0:
        l.append(i)
    else:
        if i not in l:
            l.append(i)

comb = combinations(l, 2)
final = ""
for i in comb:
    f=s
    if not isAlternate(f):
        f = f.replace(str(i[0]),"")
        f = f.replace(str(i[1]),"")
    if len(f)>len(final) and isAlternate(f):
        final = f

print(len(final))
# https://www.hackerrank.com/challenges/two-characters/problem
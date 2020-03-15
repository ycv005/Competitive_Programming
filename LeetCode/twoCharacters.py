#https://www.hackerrank.com/challenges/two-characters/problem
def isAlternate(s):
    for i in range(len(s)-2):
        if s[i]!=s[i+2]:
            return False
    return True

from itertools import combinations
n = int(input())
s = input()
t = list(set(s)) #to get all unique variable
if len(s)==1:
    # return 0
    print(0)
elif len(t)==2:
    stack=""
    for i in s:
        if len(stack)==0:
            stack+=i
        elif stack[-1]!=i:
            stack+=i
    print(len(stack))
    # return stack
else:
    final = ""
    comb = list(combinations(t, 2))
    for i in comb:
        print(i)
        f=s
        for j in f:
            if i[0]!=j and i[1]!=j:
                f=f.replace(j,"")
            if len(f)>len(final) and isAlternate(f):
                final = f
                # print("final updated-",final)
    print(len(final))
    # return len(final)
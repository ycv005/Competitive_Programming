# https://www.hackerrank.com/challenges/repeated-string/problem

s = input()
n = int(input())
tmp = n%len(s)
c = s[:tmp].count('a')
total= c+ s[tmp:].count('a')
ft = int(n/len(s))*total+ c
print(ft)
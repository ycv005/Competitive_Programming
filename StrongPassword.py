# https://www.hackerrank.com/challenges/strong-password/problem

n = int(input())
password = input()
reqp=0
if n-6<0:
    reqp= 6-n
else:
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    f1,f2,f3,f4=0,0,0,0
    for p in password:
        if f1==0 and p in numbers:
            f1=1
        if f2==0 and p in lower_case:
            f2=1
        if f3==0 and p in upper_case:
            f3=1
        if f4==0 and p in special_characters:
            f4=1
        if f1==1 and f2==1 and f3==1 and f4==1:
            break
    reqp = reqp if reqp > 4-f1-f2-f3-f4 else 4-f1-f2-f3-f4
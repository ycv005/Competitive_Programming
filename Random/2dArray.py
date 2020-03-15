l=[]
for i in range(6):
    l1= [int(i) for i in input().split(" ")]
    l.append(l1)
m =-100
for i in range(4):
    for j in range(4):
        s = l[i][j] + l[i][j+1] + l[i][j+2] + l[i+1][j+1] +l[i+2][j] + l[i+2][j+1] + l[i+2][j+2]
        # print(l[i][j] ," ", l[i+1][j] ," ", l[i+2][j] ," ", l[i+1][j+1] ," ",l[i][j+2] ," ",l[i+1][j+2] ," ",l[i+2][j+2])
        if s>m:
            m = s

print(m)
# https://www.hackerrank.com/challenges/2d-array/problem
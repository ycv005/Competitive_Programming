for t in range(int(input())):
    d={}
    for i in range(int(input())):
        s=input()
        for j in range(len(s)):
            if s[j]=='1':
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
    count=0
    for k,v in d.items():
        if v%2!=0:
            count+=1
    print(count)
# https://www.codechef.com/NOV19B/problems/SC31
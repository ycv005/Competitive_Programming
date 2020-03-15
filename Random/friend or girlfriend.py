for m in range(int(input())):
    t=int(input())
    s,x=input().split()
    list=[]
    for i in range(t):
        if(s[i]==x):
            list.append(i)

    list.append(t)

    # print(list)
    sum=0
    for i in range(1,len(list)):
        n=list[i]-list[i-1]-1
        sum=sum+int((n*(n+1)/2))
        #print(sum)
    sum=sum+int((list[0]*(list[0]+1)/2))
    #print(sum)
    print(int((t*(t+1)/2))-sum)
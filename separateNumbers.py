def separateNumbers(s):
    digit = 1
    t=""
    x=0
    flag ="NO"
    while digit<len(s) and flag=="NO":
        t=s[:digit]
        x=int(s[:digit])
        # print("x-",x)
        tmp=x
        while len(t)<len(s):
            tmp = tmp+1
            t+=str(tmp)
            # print("updated-",t)
        if t==s:
            flag="YES"
            break
        else:
            digit+=1
    if flag=="YES":
        print(flag,x)
    else:
        print(flag)
        
separateNumbers(input())
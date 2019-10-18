# https://www.hackerrank.com/challenges/sherlock-and-array/problem

def balancedSums(a):
    l,r,lp,rp=0,0,0,len(a)-1
    flag="YES"
    lf=1
    rf=1
    if len(a)==1:
        return flag
    if len(a)==2:
        if a[0]==0 or a[-1]==0:
            return flag
        else:
            return "NO"
    while rp-lp>1:
        if lp<len(a)-1 and rp>=0:
            if lf==1:
                l+=a[lp]
            if rf==1:
                r+=a[rp]
        if l>r:
            rp-=1
            lf=0
            rf=1
        elif l<r:
            lf=1
            rf=0
            lp+=1
        else:
            lp+=1
            rp-=1
            lf=1
            rf=1
            if rp-lp==1:
                rp+=1 #change anyone
                rf=0
        # print("l-",l)
        # print("r-",r)
    if l!=r and l!=0 and r!=0:
        flag="NO"
    return flag

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

T = int(input().strip())

for T_itr in range(T):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = balancedSums(arr)
    print(result)
    #     fptr.write(result + '\n')

    # fptr.close()
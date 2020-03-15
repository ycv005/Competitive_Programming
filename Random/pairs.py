#https://www.hackerrank.com/challenges/pairs/problem

def pairs(k, arr):
    arr.sort()
    count=0
    i,j=0,1
    while j<=len(arr)-1:
        if arr[j]-arr[i]==k:
            count+=1
            j+=1
        elif arr[j]-arr[i]>k:
            i+=1
        else:
            j+=1
    return count


n,k= [int(i) for i in input().split()]
l = [int(i) for i in input().split()]

print(pairs(k, l))





#-------------------------------------------------------------
# below is the binary search + two pointer solution

def getPos(nums,l,r,t):
    if l<=r:
        mid = int((l+r)/2)
        if nums[mid]==t:
            return mid
        elif nums[mid]>t: #move left
            return getPos(nums,l,mid-1,t)
        else:
            return getPos(nums,mid+1,r,t)
    else:
#      mean, l>r, since l is greater and at r some element is present
        return l

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        #getting 0's position, even 0 is not present, will get insertion position
        pos = getPos(A,0,len(A)-1,0)
        if pos==0:  #all values are positive
            return [i*i for i in A]
        elif pos==len(A): #all values are negative
            return [A[i]*A[i] for i in range(len(A)-1,-1,-1)]
        else:
            i=j=pos
            res = []
            if i-1>=0:
                i-=1
            elif j+1<len(A):
                j+=1
            while i>=0 or j<len(A):
                if i>=0 and j<len(A) and abs(A[i])>A[j]:
                    res.append(A[j]*A[j])
                    j+=1
                elif i>=0 and j<len(A):
                    res.append(A[i]*A[i])
                    i-=1
                else:
                    if i<0:
                        res+=[A[i]*A[i] for i in range(j,len(A))]
                    else:
                        res+=[A[x]*A[x] for x in range(i,-1,-1)]
                    break
            return res

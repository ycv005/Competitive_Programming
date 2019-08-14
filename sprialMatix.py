# https://www.interviewbit.com/problems/spiral-order-matrix-i/
class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        t = 0
        b = len(A)
        l = 0
        r = len(A[0])
        d = 0
        lst=[]
        # print(t, b, l, r)
        while(t<=b and l<=r):
            if(d==0):
                for i in range(l, r):
                    # print(A[t][i])
                    lst.append(A[t][i])
                t=t+1
                d = 1
            
            elif(d==1):
                for i in range(t, b):
                    # print(A[i][r])
                    lst.append(A[i][r-1])
                r=r-1
                d =2
            
            elif(d==2):
                for i in range(r-1, l-1, -1):
                    # print(A[b][i])
                    lst.append(A[b-1][i])
                b=b-1
                d = 3
            
            elif(d==3):
                for i in range(b-1, t-1, -1):
                    # print(A[i][l])
                    lst.append(A[i][l])
                d = 0
                l=l+1
        
        return lst
# https://www.codechef.com/NOV19B/problems/HRDSEQ
for t in range(int(input())):
    n = int(input())
    d={}
    # creating seq
    l=[]
    for i in range(n):
        occ = 0 
        if i==0 or i==1:
            l.append(0)
        else:
            le = l[-1]
            l_n_1 = l[:-1]
            try:
                occ = len(l_n_1) - 1 - l_n_1[::-1].index(le) + 1
            except ValueError:
                occ = -1
            if occ==-1:
                occ=0
            else:
                occ = i - occ
                # l.append(i-occ)
            l.append(occ)
        if occ in d:
            d[occ]+=1
        else:
            d[occ]=1
    
    # print(l)
    # print(d)
    print(d[l[n-1]])
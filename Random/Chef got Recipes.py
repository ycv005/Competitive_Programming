#https://www.codechef.com/MARCH19B/problems/JAIN
from collections import OrderedDict
for i in range(int(input())):
    n=int(input())
    dic = {}
    count=0
    if n==1:
        print(count)
    else:
        for j in range(n):
            tmp =sorted(list(set(input())))
            s= ''.join(tmp)
            if s in dic:
                dic[s]+=1
            else:
                dic[s]=1

    # print(dic)
    if 'aeiou' in dic:
        count+=int(((dic['aeiou']-1)*dic['aeiou'])/2)
    for k1 in list(dic):
        for k2 in dic:
            if k1=='aeiou' and k2=='aeiou':
                continue
            elif k1!=k2:
                if len(list(set(k1+k2)))==5:
                    # print("k1-",k1," k2-",k2)
                    v1=dic[k1]
                    v2=dic[k2]
                    count+=v1*v2
                    # print("count at each step",count)
        
        dic.pop(k1)
    print(count)

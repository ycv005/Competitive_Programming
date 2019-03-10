#https://www.codechef.com/MARCH19B/problems/CHDIGER
for i in range(int(input())):
    n,d= [int(i) for i in input().split()]
    dl=[]
    s=""
    mn = 10
    for j in range(len(str(n))):
        if int(str(n)[j])<=d:
            dl.append([int(str(n)[j]),j])
            if mn>int(str(n)[j]):
                mn=int(str(n)[j])
        
    if mn > d:
        mn=d
        print(str(d)*len(str(n)))
    else:
        sdl = sorted(dl,key=lambda x:x[0])
        fl=[]
        for j in range(len(sdl)):
            if j==0:
                fl.append(sdl[j])
            else:
                if fl[-1][1]<sdl[j][1]:
                    fl.append(sdl[j])
        
        for j in fl:
            s+=str(j[0])
        s+=str(d)*(len(str(n))-len(s))
        print(int(s))
        
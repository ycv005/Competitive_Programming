def lps(pat):
    lps = [0]*len(pat)
    j = 0
    i=1
    # for i in range(1,len(pat):
    while i<len(pat):
        if pat[j]==pat[i]:
            j+=1
            lps[i]=j
        elif j>0:
            j = lps[j-1]
            i-=1
        else:
            lps[i]=0
        i+=1
    return lps

pattern = "aabaabaaa"
print("here is the shift array-",lps(pattern))

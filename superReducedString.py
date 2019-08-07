def superReducedString(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            s=s[:i] + s[i+2:]
            break
    return s

s= input()
a=s
while(len(s)):
    s = superReducedString(s)
    # print("value",s)
    if(len(a)==len(s)):
        break
    a=s

if(len(s)):
    print(s)
else:
    print("Empty String")
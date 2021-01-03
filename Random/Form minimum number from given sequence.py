for _ in range(int(input())):
    s = input()
    # stack
    st = []
    currHighest = 0
    res = ""
    i = 0
    while i < len(s):
        c = s[i]
        currHighest += 1
        if c == "I":
            res += str(currHighest)
        else:
            while s[i] != "I":
                c = s[i]
                st.append(c)
                i += 1
                if i == len(s):
                    break
            # if i == len(s):
            #     pass
            # else:
            currHighest += len(st)
            tmp = currHighest
            while len(st) > 0:
                st.pop()
                res += str(tmp)
                tmp -= 1
            # add for I or ending part
            res += str(tmp)
            # if I is last
        if i == len(s)-1:
            res += str(currHighest + 1)

        i += 1
    print(res)

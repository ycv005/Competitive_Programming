alpha = "abcdefghijklmnop"


def decodeStrOfFour(s, i, j):
    res = ""
    x = 1
    y = len(alpha)
    while i < j and i < len(s):
        c = s[i]
        if c == '0':
            y -= (y-x + 1) // 2
        else:
            x += (y-x + 1)//2

        i += 1

    # print("x, y- ", x-1, y-1)
    res = alpha[x-1:y]
    # print("res-", res)
    return res


for t in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    decoded_str = ""
    while i < len(s):
        tmp_decoded = decodeStrOfFour(s, i, i+4)
        # print("tmp-", tmp_decoded)
        decoded_str += tmp_decoded
        i += 4
    print(decoded_str)

for t in range(int(input())):
    n = int(input())
    res = []
    dic = {}
    max_tweet = 1
    for _ in range(n):
        un, tid = input().split()
        if un in dic:
            dic[un] += 1
            max_tweet = dic[un] if dic[un] > max_tweet else max_tweet
        else:
            dic[un] = 1
    # case of no tweet
    if len(dic) == 0:
        print("None")
    else:
        for un, v in dic.items():
            if v == max_tweet:
                res.append([un, v])
        res.sort(key=lambda x: x[0])
        for r in res:
            print(r)

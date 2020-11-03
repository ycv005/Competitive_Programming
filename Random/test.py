for t in range(int(input())):
    n = int(input())
    s = input()
    sm = 0
    for i, c in enumerate(s):
        sm += ord(c) - 97

    while len(str(sm)) != 1:
        tm = 0
        n = sm
        while n >= 1:
            d = n % 10
            tm += d
            n = n//10
        sm = tm
    print(chr(sm+97))

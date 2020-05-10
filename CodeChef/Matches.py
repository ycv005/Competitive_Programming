# https://www.codechef.com/MAY19B/problems/MATCHS
for t in range(int(input())):
    n, m = map(int, input().split())
    ari_turn  = True
    bigger_pile = n if n>=m else m
    smaller_pile = m if bigger_pile == n else n

    while bigger_pile%smaller_pile != 0 and bigger_pile//smaller_pile<=1: # if anyone get empty, game ends
        bigger_pile = bigger_pile%smaller_pile
        print("result in-between-",bigger_pile, smaller_pile)
        ari_turn = not ari_turn
        bigger_pile, smaller_pile = smaller_pile, bigger_pile

    if not ari_turn:
        print("Rich")
    else:
        print("Ari")

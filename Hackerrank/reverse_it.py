def isPalindrome(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


s = input().split()
pal = []
for i, word in enumerate(s):
    if isPalindrome(word):
        pal.append(word)

    if i < len(s)-1:
        print(word[::-1]+" ", end="")
    elif i == len(s)-1:
        print(word[::-1])


if len(pal) == 0:
    print("NO PALINDROMES")
else:
    for i, v in enumerate(pal):
        print(v)

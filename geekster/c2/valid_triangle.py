def isValidTriangle(a, b, c):
    if a+b+c == 180:
        return True
    return False


a, b, c = list(int(i)
               for i in input("Enter all 3 degree of the triangle to check its validity- ").split())
print(isValidTriangle(a, b, c))

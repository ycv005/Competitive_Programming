def getAbsoluteNumber(num):
    if num < 0:
        num *= -1
    return num


n = int(input("Enter the number, to get its absolute value= "))
print(getAbsoluteNumber(n))

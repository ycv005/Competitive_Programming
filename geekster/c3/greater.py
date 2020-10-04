def threeOfGreater(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:  # may be both equal num3 , num2
            return num3
    elif num2 > num3:
        return num2
    else:
        return num3


num1, num2, num3 = list(int(i) for i in input().split())

print(threeOfGreater(num1, num2, num3))

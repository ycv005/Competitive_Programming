def isLeapYear(yr):
    if yr % 4 == 0 and yr % 100 == 0 and yr % 400 == 0:
        return True
    return False


yr = int(input("Enter a yr to check whether it is a leap year or not"))

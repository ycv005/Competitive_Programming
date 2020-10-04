def calculateGrade(a, b, c):
    val = (a + b + c)//3  # floor
    if 90 <= val and val <= 100:
        return "A"
    elif 80 <= val and val <= 89:
        return "B"
    elif 70 <= val and val <= 79:
        return "C"
    elif 60 <= val and val <= 69:
        return "D"
    elif 0 <= val and val <= 59:
        return "E"
    else:
        return "Wrong numbers provided"


a, b, c = list(int(i)
               for i in input("Enter all 3 marks to get the average- ").split())
print(calculateGrade(a, b, c))

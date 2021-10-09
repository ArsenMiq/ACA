year = int(input())

century = 0

if year % 100 > 0:
    century = (year // 100) + 1
else:
    century = year // 100

print("The century of year ", year, " is ", century)

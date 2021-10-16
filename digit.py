number = int(input("Set a number - "))

digit = 1

while number > 0:
    point = number % 10
    if point != 0:
        digit *= number % 10
    number //= 10

print("Digit product is : ", digit)

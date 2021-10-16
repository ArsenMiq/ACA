number = int(input("Set a number : "))

point = number

count = 0

while point > 0:
    if number % point == 0:
        count += 1
    point -= 1

print("The count of divisors : ", count)

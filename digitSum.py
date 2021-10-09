number = int(input())
digSum = 0

while number > 0:
    a = number % 10
    digSum += a
    number //=10

print("Sum of digits: ", digSum)

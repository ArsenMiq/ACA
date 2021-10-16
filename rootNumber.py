def get_sum_of_digits(number):
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s


number = int(input("Set a number : "))

sumDigits = number
print("The sum of digits\n", number)
while sumDigits >= 10:
    sumDigits = get_sum_of_digits(sumDigits)
    print(sumDigits)

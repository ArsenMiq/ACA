import math

def isPrime(num):
    p = round(math.sqrt(num))
    for i in range(2, p+1):
        if num % i == 0:
            return False
    return True


def goldBach(num):
    for i in range(2, num // 2 + 1):
        if(isPrime(i) and isPrime(num - i)):
            return i, num - i

number = int(input("Set a number: "))
print(goldBach(number))

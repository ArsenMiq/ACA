def isPalindrome(n):
    p = 0
    k = n
    while k > 0:
        p *= 10
        p += k % 10
        k //= 10
    return p == n

def getPalindromes(a, b):
    lst = []
    for i in range(a, b):
        if isPalindrome(i):
            lst.append(i)
    return lst

a = int(input())
b = int(input())
print("Output: ", getPalindromes(a, b))

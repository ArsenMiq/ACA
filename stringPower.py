def getPower(s, k):
    neg = s[:len(s) // abs(k)]
    if k >= 0:
        return s * k
    elif s.count(neg) == abs(k):
        return neg
    else:
        return "Undefined"


s = input("Input a string : ")
k = int(input("k = "))
print(getPower(s, k))

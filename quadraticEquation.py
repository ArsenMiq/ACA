import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("Non-quadratic equation")
    if b == 0 and c == 0:
        print("Infinite solutions")
        exit()
    x = -c / b
    print("One solution: ", x)
else:
    print("Quadratic equation")
    d = b*b - 4*a*c
    print("Discriminant: ", d)
    if d <= 0:
        print("No Solutions")
        exit()
    x1 = (-b + math.sqrt(d)) / 2*a
    x2 = (-b - math.sqrt(d)) / 2*a
    s1 = a*x1*x1 + b*x1 + c
    s2 = a*x2*x2 + b*x2 + c

    if s1 == 0 and s2 == 0:
        print("Two solutions: ", x1, x2)
    elif s1 == 0:
        print("One solution: ", x1)
    elif s2 == 0:
        print("One solution: ", x2)
    else:
        print("No Solutions")

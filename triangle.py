a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

p = a**2 + b**2

if a == b and b == c:
    print("Acute Triangle")
elif p < c**2:
    print("Obtuse Triangle")
elif p == c**2:
    print("Right Triangle")
else:
    print("No Triangle")

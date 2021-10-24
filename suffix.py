arr = [float(item) for item in input("Enter the list items : ").split()]

s = sum(arr)

for i in range(1, len(arr) + 1):
    print(s)
    s = s - arr[i - 1]

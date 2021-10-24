n = int(input())
s = int(input())
arr = [int(item) for item in input("Enter the list items : ").split()]

s = s % n
print(arr[-s:] + arr[:-s])

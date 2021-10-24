def tree(num):
    for i in range(1, num + 1, 2):
        l = (num - i) // 2
        print(" " * l, "*" * i)
    
num = int(input())
tree(num)

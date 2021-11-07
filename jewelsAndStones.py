jewels = input("Input jewels : ")
stones = input("Input stones : ")

print(sum([stones.count(each) for each in jewels]))

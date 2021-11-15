def transpose(matrix):
    return [*zip(*matrix)]

matrix = [[2,4,-1],
        [-10,5,11],
        [18,-7,6]]

print(transpose(matrix))

matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

print(transpose(matrix))

matrix = [[1,2,3],
        [4,5,6]]

print(transpose(matrix))

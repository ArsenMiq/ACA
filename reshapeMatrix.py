def reshape(matrix, r, c):
    if r * c == len(matrix) * len(matrix[0]):
        data = [nb for row in matrix for nb in row]
        return [[data[c * i + j] for j in range(c)] for i in range(len(data)//c)]
    else:
        return matrix



matrix = [[1,2],
        [3,4]]

r = 1
c = 4
print(reshape(matrix, r, c))

class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        TODO: implement
        """
        with open(filename, 'w') as f:
            f.write(self._matrix)
    
    def transpose(self):
        """
        Transpose the matrix.
        TODO: implement
        """
        return [*zip(*self._matrix)]


    @property
    def shape(self):
        return self._columns, self._rows

    @property
    def zeros_matrix(rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)
        return M


    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        TODO: implement
        """
        if self._rows != other._rows or self._columns != other._columns:
            raise ArithmeticError('Matrices are NOT the same size.')

        C = zeros_matrix(len(self._rows), len(other._columns))

        for i in range(self._rows):
            for j in range(other._cols):
                C[i][j] = A[i][j] + B[i][j]

        return C


    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.
        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        TODO: implement
        """
        rowsA = len(self._rows)
        colsA = len(self._matrix[0])
        rowsB = len(other._rows)
        colsB = len(B[0])
        if colsA != rowsB:
            raise ArithmeticError('Number of A columns must equal number of B rows.')

        C = zeros_matrix(rowsA, colsB)
        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for ii in range(colsA):
                    total += A[i][ii] * B[ii][j]
                C[i][j] = total

        return C


    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        TODO: implement
        """

    @property
    def trace(self):
        """
        Find the trace of the matrix.
        TODO: implement
        """
        size = len(self._rows)

        tr = 0
        for i in size:
            tr += size[i][i]
        return tr

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """
        A = self._matrix
        total = 0
        indices = list(range(len(A)))

        if len(A) == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val

        for fc in indices:
            As = A
            As = As[1:]
            height = len(As)

            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc+1:]

            sign = (-1) ** (fc % 2)
            sub_det = det(As)
            total += sign * A[0][fc] * sub_det

        return total

m1 = Matrix(list = [[1,2],[3,4]])
m2 = Matrix(list = [[1,0],[0,1]])
print("Matrix determinant : ", m1.determinant)
print("Matrix transpose : ", m1.transpose)
print("Matrix add : ", m1 + m2)
print("Matrix multiply : ", m1 * m2)

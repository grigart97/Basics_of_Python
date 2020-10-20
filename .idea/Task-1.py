class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for raw in self.matrix:
            for el in raw:
                str_matrix += f'{el:3d}'
            str_matrix += '\n'
        return str_matrix


    def __add__(self, other):
        try:
            sum_matrix = []
            for i in range(len(self.matrix)):
                raw_matrix = []
                for j in range(len(self.matrix[i])):
                    raw_matrix.append(self.matrix[i][j] + other.matrix[i][j])
                sum_matrix.append(raw_matrix)
            return Matrix(sum_matrix)
        except IndexError:
            return 'Вы пытаетесь сложить матрицы разных размеров'

a = Matrix([[1, 2, 3, 7], [3, 4, 5, 2], [5, 6, 7, 6]])
b = Matrix([[9, 8, 7, 9], [7, 6, 5, 3], [5, 4, 3, 12]])
print(a)
print(b)
print(a + b)

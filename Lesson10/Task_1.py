####################################################################################################################
# Задание 1                                                                                                        #
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен #
# принимать данные (список списков) для формирования матрицы.                                                      #
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.                     #
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).            #
# Результатом сложения должна быть новая матрица.                                                                  #
####################################################################################################################

class Matrix():
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for row in self.matrix:
            for el in row:
                str_matrix += (str(el) + '  ')
            str_matrix = str_matrix[:-2] + '\n'
        return str_matrix[:-1]

    def __add__(self, other):
        if isinstance(other, Matrix):
            rowA, colA = self.getSize
            rowB, colB = other.getSize
            if (rowA == rowB) and (colA == colB):
                mx = []
                for row, el_row in enumerate(self.matrix):
                    mr = []
                    for col, el_col in enumerate(el_row):
                        mr.append(el_col + other.matrix[row][col])
                    mx.append(mr)
                return Matrix(mx)
            else:
                print(f"Ошибка! Для сложения матрицы должны быть одинакового размера.")
                print(f"Размер матрицы {self.getName}: {rowA} x {colA}")
                print(f"Размер матрицы {other.getName}: {rowB} x {colB}")
                print("Сложение матриц не произведено...")
                return self
        else:
            print("Ошибка! Для сложения второе слагаемое должна быть матрицей.")
            print("Сложение матриц не произведено...")
            return self

    @property
    def getName(self):
        for i, j in globals().items():
            if j is self:
                return i

    @property
    def getSize(self):
        row = len(self.matrix)
        if row > 0:
            col = len(self.matrix[0])
        return row, col


matrix = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
matrix2 = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
m_1 = Matrix(matrix)
print("Матрица A:")
print(m_1)
m_2 = Matrix(matrix2)
print("Матрица B:")
print(m_2)
m_3 = Matrix(matrix)
print("Матрица C:")
print(m_3)
print("Результат сложения матрицы A и значения:")
print(m_1 + 7)
print("Результат сложения матриц A + B:")
print(m_1 + m_2)
print("Результат сложения матриц A + C:")
print(m_1 + m_3)

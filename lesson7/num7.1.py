"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно
— первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix):

        self.matrix = matrix

    def __str__(self):
        res = ""
        for line in self.matrix:
            for el in line:
                res += str(el) + " "

            res += "\n"

        return res

    def __add__(self, other):
        line = []
        new_matrix = []
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    line.append(self.matrix[i][j] + other.matrix[i][j])
                new_matrix.append(line)
                line = []

            return Matrix(new_matrix)
        else:
            return "Неверный размер"


print("Урок 7. Пункт 1")


class Matrix(object):
    def __init__(self, matrix_rows):
        self.matrix_rows = matrix_rows
        # Заполнение матрицы

    def __str__(self):
        return "\n".join(str(rows) for rows in self.matrix_rows)
    # Вывод строк матрицы с переходом на следующую строку на каждом

    def __add__(self, sum_parameter):
        self.result = [[0 for ind_columns in range(len(self.matrix_rows[0]))]
                       for row_index in range(len(self.matrix_rows))]
        # Создана матрица соответствующего размера для дальнейшего сложения в неё
        for ind_rows in range(len(self.matrix_rows)):
            for ind_columns in range(len(self.matrix_rows[0])):
                self.result[ind_rows][ind_columns] = self.matrix_rows[ind_rows][ind_columns] + \
                                                       sum_parameter.matrix_rows[ind_rows][ind_columns]
        # Поэлементное сложение матриц
        return Matrix(self.result)


matrix_1 = Matrix([[2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2], [0, 0, 0, 0]])
matrix_2 = Matrix([[2, 2, 2, 2], [4, 4, 4, 4], [1, 7, 1, 7], [2, 2, 2, 2]])
print(f"Первая матрица: \n{matrix_1}")
print(f"Вторая матрица: \n{matrix_2}")
print(f"Результат сложения матриц: \n{matrix_1 + matrix_2}")

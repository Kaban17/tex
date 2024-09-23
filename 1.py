import numpy as np
import scipy.linalg as sla
def my_det(matrix):
    # Проверка, является ли матрица квадратной
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Матрица не является квадратной")

    # Копирование матрицы для избежания изменения оригинальной матрицы
    mat = matrix.astype(float)
    n = mat.shape[0]  # Размерность квадратной матрицы
    det = 1

    # Прямой ход метода Гаусса для приведения матрицы к верхнетреугольному виду
    for i in range(n):
        # Поиск максимального элемента в текущем столбце
        max_row = np.argmax(np.abs(mat[i:, i])) + i

        # Обмен строк для уменьшения ошибок округления
        if i != max_row:
            mat[[i, max_row]] = mat[[max_row, i]]
            # Инвертирование определителя при обмене строк
            det *= -1

        # Приведение матрицы к верхнетреугольному виду
        for j in range(i + 1, n):
            factor = mat[j, i] / mat[i, i]
            mat[j, i:] -= factor * mat[i, i:]

    # Вычисление определителя как произведения элементов главной диагонали
    det *= np.prod(np.diagonal(mat))

    return det

# Пример использования
# Запустите этот блок кода
for _ in range(50):
    X = np.random.rand(50, 50)
    if np.abs(my_det(X) - sla.det(X)) > 1e-6:
        print('FAILED')

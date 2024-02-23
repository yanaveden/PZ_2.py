# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
import random


def elements(matrix):
    return any(any(element > 0 for element in row) for row in matrix)


N = int(input("Введите размерность матрицы: "))
matrix = [[random.randint(-10, 10) for el in range(N)] for row in range(N)]

print("Матрица:")
[print(i) for i in matrix]
print(f"Результат проверки на наличие положительных элементов: {elements(matrix)}")
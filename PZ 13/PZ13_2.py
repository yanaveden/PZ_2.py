# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.

def elements(matrix):
    for row in matrix:
        for element in row:
            if element > 0:
                return True
    return False

matrix = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

result = elements(matrix)
print("\nРезультат проверки на наличие положительных элементов:")
print(result)
# В квадратной матрице все элементы, не лежащие на главной
# диагонали увеличить в 2 раза.

matrix = [[i+j for j in range(1, 4)] for i in range(3)]
print("Матрица до изменений: ")
[print(i) for i in matrix]


def non_diagonal(matrix):
    return [[matrix[i][j] * 2 if i != j else matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]


print("Матрица после изменений:")
[print(i) for i in non_diagonal(matrix)]

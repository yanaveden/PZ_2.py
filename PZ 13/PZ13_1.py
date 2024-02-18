# В квадратной матрице все элементы, не лежащие на главной
# диагонали увеличить в 2 раза.

def diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                matrix[i][j] *= 2

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal(matrix)
print("Матрица после увеличения элементов в 2 раза:")
for row in matrix:
    print(row)

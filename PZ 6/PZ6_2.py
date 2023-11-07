# Дан список размера N. Найти номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

import random


def find_index(arr):
    n = len(arr)
    last_max = 0
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            last_max = i
    return last_max


N = int(input('Введите размер списка: '))
G = []
i = 0
while i < N:
    G.append(random.randint(0, 50))
    i += 1

max_index = find_index(G)
print("Список:", G)
print('Максимальный элемент списка: ', G[max_index])
print("Index последнего локального максимума:", max_index)

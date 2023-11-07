# Дан список размера N. Переставить в обратном порядке элементы список, расположенные между
# его минимальным и максимальным элементами, включая минимальный и максимальный элементы
import random


def reverse_elements_between_min_and_max(arr):
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    start_index = min([min_index, max_index])
    end_index = max([min_index, max_index])
    arr = arr[:start_index] + arr[start_index:end_index + 1][::-1] + arr[end_index + 1:]
    return arr

N = int(input('Введите размер списка: '))
G = []
i = 0
while i < N:
    G.append(random.randint(0,100))
    i += 1
print("Список:", G)
print('Максимальный элемент списка: ', max(G))
print('Минимальный элемент списка: ', min(G))
G = reverse_elements_between_min_and_max(G)
print("Список после перестановки:", G)
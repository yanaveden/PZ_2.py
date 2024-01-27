#1.	Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Элементы, умноженные на максимальный элемент:

import random

with open("sequence.txt", "w") as file:
    sequence_length = 10
    sequence = [random.randint(-10, 10) for _ in range(sequence_length)]
    file.write(' '.join(map(str, sequence)))

min_element = min(sequence)
max_element = max(sequence)

multiplied_sequence = [element * max_element for element in sequence]

with open('file.txt', 'w') as file:
    file.write(f"Initial data: {sequence}\n")
    file.write(f"Number of elements: {len(sequence)}\n")
    file.write(f"Minimum element:: {min_element}\n")
    file.write("Elements multiplied by the maximum element:\n")
    for element in multiplied_sequence:
        file.write(f"{element}\n")

# В последовательности на n целых чисел умножить
# элементы до n-1 на элемент n.

def multiply_elements(sequence):
    multiplied_sequence = list(map(lambda x: x * sequence[-1], sequence[:-1]))
    return multiplied_sequence


s = [1, 2, 3, 4, 5, 6]
print(multiply_elements(s))
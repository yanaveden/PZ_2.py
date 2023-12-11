# Дан словарь с четным количеством элементов. Найти суммы значений элементов
# первой и второй половин с использованием функции. Результаты вывести на экран.

def sum_half_of_dict(d):
    half_len = len(d) // 2
    sum_first_half = sum(list(d.values())[:half_len])
    sum_second_half =  sum(list(d.values())[half_len:])

    return sum_first_half, sum_second_half

my_dict = {'a': 2, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 1}

result = sum_half_of_dict(my_dict)
print("Сумма значений первой половины словаря:", result[0])
print("Сумма значений второй половины словаря:", result[1])


# Дано целое число N. Используя операции деления нацело и взятия остатка
# Найти число, полученное при прочтении числа N справа налево.
number = input("Введите число:")

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print('Неправильно ввели!')
        number = input('Введите число: ')

reversed_n = 0
while number != 0:
    reversed_n = reversed_n * 10 + (number % 10)
    number //= 10

print("Перевёрнутое число:", reversed_n)
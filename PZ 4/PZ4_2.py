N = int(input("Введите целое число: "))

try:
    if N <= 0:
        raise ValueError
except ValueError:
    N = int(input("Некорректный ввод! Введите целое число больше 0:"))

reversed_number = N // 10 % 10
print("Число, полученное при прочтении числа N справа налево:", reversed_number)
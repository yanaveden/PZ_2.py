price = float(input("Введите цену 1 кг конфет: "))
for i in range(1, 11):
    print("Стоимость", i/10, "кг конфет составляет:", price * i/10)
V1 = int(input("Введите скорость первого автомобиля (км/ч): "))
V2 = int(input("Введите скорость второго автомобиля (км/ч): "))
S = int(input("Введите начальное расстояние между автомобилями (км): "))
T = int(input("Введите время (часы): "))

result = S + (T * (V1 + V2))
print("Расстояние между автомобилями через", T, "часа:", result, "км")

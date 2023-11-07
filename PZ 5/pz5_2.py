# Описать функцию RectPS(x1,y1,х2,y2,P,S), вычисляющую периметр P и площадь S прямоугольника со сторонами,
# параллельными осям координат, по координатам (х1, y1), (х2, y2) его противоположных вершин
# (x1, y1, x2, y2 — входные, P и S — выходные параметры вещественного типа).
# С помощью этой функции найти периметры и площади трех прямоугольников с данными противоположными вершинами.
def RectPS(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    P = 2 * (width + height)
    S = width * height
    return P, S

i = 1
while i <= 3:

    x1 = input('Введите x1: ')
    while type(x1) != float:
        try:
            x1 = float(x1)
        except ValueError:
            print('Неправильно ввели!')
            x1 = input('Введите x1: ')


    x2 = input('Введите x2: ')
    while type(x2) != float:
        try:
            x2 = float(x2)
        except ValueError:
            print('Неправильно ввели!')
            x2 = input('Введите x2: ')

    y1 = input('Введите y1: ')
    while type(y1) != float:
        try:
            y1 = float(y1)
        except ValueError:
            print('Неправильно ввели!')
            y1 = input('Введите y1: ')

    y2 = input('Введите y2: ')
    while type(y2) != float:
        try:
            y2 = float(y2)
        except ValueError:
            print('Неправильно ввели!')
            y2 = input('Введите y2: ')

    P, S = RectPS(x1, y1, x2, y2)
    print("Прямоугольник ", i)
    print("Периметр: ", P)
    print("Площадь: ", S)
    print()
    i += 1



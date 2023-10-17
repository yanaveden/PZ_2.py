a, b = input('Введите число a: '), input('Введите число b: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите число a: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели!')
        b = input('Введите число b: ')
        
if a>2 and b<3:
    print('Неравенства a>2 и b<3 справедливы')
elif a<=2 and b<3:
    print('Неравенство a>2 несправедливо')
elif a>2 and b>=3:
    print('Неравенство b<3 несправедливо')
else:
    print('Оба неравенства несправедливы')



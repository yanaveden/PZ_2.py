# Дана строка-предложение. Зашифровать ее, поместив вначале все символы, расположенные на четных позициях строки,
# а затем, в обратном порядке, все символы, расположенные на нечетных позициях
# (например, строка «Программа» превратится в «ргамамроП»)

def string(input_string):
    even = input_string[::2]
    odd = input_string[1::2][::-1]
    all = even + odd
    reversed = all[::-1]
    return reversed

original_string = input("Введите слово или предложение: ")
print(string(original_string))


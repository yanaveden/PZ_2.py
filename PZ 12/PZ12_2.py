# Составить генератор (yield), который выводит из строки только буквы.

def letters_only(input_str):
    for char in input_str:
        if char.isalpha():
            yield char


input_string = "Hello, 123 World!"
letters = ''.join(letters_only(input_string))
print(letters)
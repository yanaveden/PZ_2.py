# Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив
# символы верхнего регистра на нижний.

with open('text18-4.txt', 'r', encoding='utf16') as file:
    content = file.read()
    print(content)

num_letters = sum(i.isalpha() for i in content)
print("Количество букв в тексте: ", num_letters)

poem = content.lower()

with open('poem.txt', 'w', encoding='utf16') as file:
    file.write(poem)

print("Текст в стихотворной форме создан и сохранен в файл poem.txt")



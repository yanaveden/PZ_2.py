from typing import Pattern
import re

with open("file", encoding="utf-8") as f:
    text = f.read()


def get_text(pattern: Pattern[str]) -> str:
    return ', '.join(pattern.findall(text))


ex1 = re.compile(r"\d+")
print(f"Все натуральные числа: {get_text(ex1)}\n")

ex2 = re.compile(r"[A-ZА-Я]+")
print(f"Все «слова», написанные капсом: {get_text(ex2)}\n")

ex3 = re.compile(r"[А-Я][0-9].")
print(f"Все слова, в которых есть русская буква, а за ней цифра: {get_text(ex3)}\n")

ex4 = re.compile(r"\b[А-ЯA-ZЁ]\w*\b")
print(f"Все слова, начинающиеся с русской или латинской большой букв: {get_text(ex4)}\n")

ex5 = re.compile(r"\b[АЕЁИОУЫЭЮЯaeiou]\w+")
print(f"Все слова, которые начинаются на гласную: {get_text(ex5)}\n")

ex6 = re.compile(r"\B\d+\B")
print(f"Все натуральные числа, не находящиеся на границе слова: {get_text(ex6)}\n")

ex7 = re.compile(r".*\*.*",)
print(f"Найдите строчки, в которых есть символ * (. — это точно не конец строки!): {get_text(ex7)}\n")

ex8 = re.compile(r"\(.*?\)+")
print(f"Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки: {get_text(ex8)}\n")

ex9 = re.compile(r'<a href="#\d+">.*</a>')
print(f"Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами): \n{get_text(ex9)}\n")

ex10 = re.compile(r'<a href="#\d+">(.*?)</a>')
print(f"Выделите одним махом только текстовую часть оглавления, без тегов: {get_text(ex10)}\n")

ex11 = re.compile(r"^\s*$")
print(f"Найдите пустые строчки: {get_text(ex11)}\n")

ex12 = re.compile(r'(<a href="#\d+">).*?(</a>)')
print("Все теги, не включая их содержимое: ")
[print(f"{tags}") for tags in map(lambda x: " ".join(x), ex12.findall(text))]
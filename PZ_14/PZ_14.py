# В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
# фразу «Министерства образования Ростовской области», посчитать количество
# произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
# «50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re
# 1
with open('hotline.txt', 'r', encoding='utf-8') as file:
    text = file.read()

new_text, count_additions = re.subn(r'Горячая линия', r'Горячая линия Министерства образования Ростовской области', text)

with open('hotline.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)

print('Количество произведенных добавлений:', count_additions)

# 2
phone_numbers_03 = re.findall(r'\b\d[0-9]{7,}03\b', text)
phone_numbers_50 = re.findall(r'\b\d[0-9]{7,}50\b', text)

count_phone_numbers_03 = len(phone_numbers_03)
count_phone_numbers_50 = len(phone_numbers_50)

print(f'Количество номеров телефонов, заканчивающихся на "03": {count_phone_numbers_03}')
print(f'Количество номеров телефонов, заканчивающихся на "50": {count_phone_numbers_50}')

# 3
ege_gia_numbers = re.findall(r'Горячая линия.*ЕГЭ.*|Горячая линия.*ГИА.*', text)
print('Номера телефонов горячих линий, связанных с ЕГЭ/ГИА:')
for number in ege_gia_numbers:
    print(number)
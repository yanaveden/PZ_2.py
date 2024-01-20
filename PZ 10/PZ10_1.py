#Определить в каких магазинах можно приобрести книги Маяковского

Magistr = {'Лермонтов', 'Достоевский', 'Маяковский', 'Тютчев'}
DomKnigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
BookMarket = {'Пушкин', 'Достоевский', 'Достоевский'}
Gallereya = {'Чехов', 'Пушкин', 'Тютчев'}

stores_with_mayakovsky = set()

if 'Маяковский' in Magistr:
    stores_with_mayakovsky.add('Магистр')
if 'Маяковский' in DomKnigi:
    stores_with_mayakovsky.add('ДомКники')
if 'Маяковский' in BookMarket:
    stores_with_mayakovsky.add('Букмаркет')
if 'Маяковский' in Gallereya:
    stores_with_mayakovsky.add('Галерея')

print("Книги Маяковского можно приобрести в следующих магазинах:", stores_with_mayakovsky)
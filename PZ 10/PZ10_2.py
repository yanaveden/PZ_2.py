Magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
DomKnigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
BookMarket = {'Пушкин', 'Достоевский', 'Маяковский'}
Gallereya = {'Чехов', 'Пушкин', 'Тютчев'}
mayakovski_books = []

if 'Маяковский' in Magistr:
    mayakovski_books.append('Магистр')
if 'Маяковский' in DomKnigi:
    mayakovski_books.append('ДомКниги')
if 'Маяковский' in BookMarket:
    mayakovski_books.append('Букмаркет')
if 'Маяковский' in Gallereya:
    mayakovski_books.append('Галлерея')

print(f"Книги Маяковского можно приобрести в следующих магазинах: {', '.join(mayakovski_books)}\n")

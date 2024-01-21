MAGISTER = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
DOM_KNIGI = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
BOOK_MARKET = {'Пушкин', 'Достоевский', 'Маяковский'}
GALLERY = {'Чехов', 'Пушкин', 'Тютчев'}

kniga_mayak = "Маяковский"

mayakovski_byu = [name for name, s in
                  [("Магистр", MAGISTER), ("ДомКниги", DOM_KNIGI), ("БукМаркет", BOOK_MARKET), ("Галерея", GALLERY)] if
                  kniga_mayak in s]

print(f"Книги Маяковского можно приобрести в следующих магазинах: {', '.join(mayakovski_byu)}\n")
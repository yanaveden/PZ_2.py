# Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
# источников в библиотеке. БД должна содержать таблицу Каталог с информацией о
# книгах и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
# Название книги, Год выпуска, Аннотация.

import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Создание таблицы Каталог
c.execute('''CREATE TABLE IF NOT EXISTS Catalog
                 (book_code TEXT PRIMARY KEY, genre TEXT, country TEXT, series TEXT, author TEXT, title TEXT, year INTEGER, annotation TEXT)''')

# Функция для добавления новой книги
def add_book(book_code, genre, country, series, author, title, year, annotation):
    c.execute("INSERT INTO Catalog VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (book_code, genre, country, series, author, title, year, annotation))
    conn.commit()
    print("Книга успешно добавлена в каталог.")

# Функция для поиска книги по коду
def search_book(book_code):
    c.execute("SELECT * FROM Catalog WHERE book_code=?", (book_code,))
    book = c.fetchone()
    if book:
        print(f"Код книги: {book[0]}")
        print(f"Жанр: {book[1]}")
        print(f"Страна издания: {book[2]}")
        print(f"Серия: {book[3]}")
        print(f"Автор: {book[4]}")
        print(f"Название книги: {book[5]}")
        print(f"Год выпуска: {book[6]}")
        print(f"Аннотация: {book[7]}")
    else:
        print("Книга не найдена в каталоге.")

# Пример использования
add_book("B001", "Фантастика", "США", "Звездные войны", "Джордж Лукас", "Новая надежда", 1977, "Эпическая космическая опера...")
search_book("B001")

# Закрытие соединения с базой данных
conn.close()

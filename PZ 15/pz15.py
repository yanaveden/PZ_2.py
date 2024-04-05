# Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
# источников в библиотеке. БД должна содержать таблицу Каталог с информацией о
# книгах и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
# Название книги, Год выпуска, Аннотация.

import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS katalog (
    id_knigi INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT,
    country TEXT,
    seria INTEGER,
    author TEXT,
    name_knigi TEXT,
    god INTEGER,
    annotation TEXT
)
''')

knigi = [
    (None, "Фантастика", "Россия", 1, "Аркадий и Борис Стругацкие", "Хромая судьба", 1965, "История о космической экспедиции, которая терпит крушение на неизвестной планете."),
    (None, "Детектив", "США", 2, "Агата Кристи", "Десять негритят", 1939, "Классический детектив о загадочных убийствах на острове."),
    (None, "Фэнтези", "Великобритания", 3, "Дж. Р. Р. Толкин", "Властелин колец", 1954, "Эпическая сага о кольце власти и приключениях хоббита Фродо."),
    (None, "Роман", "Франция", 4, "Виктор Гюго", "Отверженные", 1862, "История борьбы бывшего каторжника Жана Вальжана за справедливость."),
    (None, "Драма", "Греция", 5, "Софокл", "Царь Эдип", -458, "Трагедия о проклятии Царя Эдипа и его попытках избежать судьбы."),
    (None, "Приключения", "Италия", 6, "Александр Дюма", "Граф Монте-Кристо", 1844, "Роман о мести и приключениях Эдмонда Дантеса."),
    (None, "Юмор", "США", 7, "Марк Твен", "Приключения Тома Сойера", 1876, "Приключенческий роман о мальчике Томе и его друзьях."),
    (None, "Ужасы", "Ирландия", 8, "Брэм Стокер", "Дракула", 1897, "Классический роман о вампире Графе Дракуле и его преследователе Ван Хельсинге."),
    (None, "Научная фантастика", "США", 9, "Филип К. Дик", "Мечтают ли андроиды об электроовцах?", 1968, "Роман о мире, где андроиды и люди сосуществуют."),
    (None, "Исторический роман", "Великобритания", 10, "Джордж Р. Р. Мартин", "Игра престолов", 1996, "Эпическая сага о борьбе за Железный Трон в вымышленном мире."),
]

cursor.executemany('''
INSERT INTO katalog (id_knigi, genre, country, seria, author, name_knigi, god, annotation)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', knigi)

def dropTable():
    cursor.execute('DROP TABLE IF EXISTS katalog')
    conn.commit()

def getkniga():
    cursor.execute('SELECT * FROM katalog')
    return cursor.fetchall()

for knigi in getkniga():
    print(knigi)

conn.commit()
conn.close()

# Поиск
def find_book_by_name(book_name):
    cursor.execute("SELECT * FROM katalog WHERE name_knigi=?", (book_name,))
    return cursor.fetchone()

def find_books_by_author_and_country(author, country):
    cursor.execute("SELECT * FROM katalog WHERE author=? AND country=?", (author, country))
    return cursor.fetchall()

def find_books_by_genre(genre):
    cursor.execute("SELECT * FROM katalog WHERE genre=?", (genre,))
    return cursor.fetchall()

# Удаление
def delete_book_by_name(book_name):
    cursor.execute("DELETE FROM katalog WHERE name_knigi=?", (book_name,))
    conn.commit()

def delete_books_by_author_and_country(author, country):
    cursor.execute("DELETE FROM katalog WHERE author=? AND country=?", (author, country))
    conn.commit()

def delete_books_by_genre(genre):
    cursor.execute("DELETE FROM katalog WHERE genre=?", (genre,))
    conn.commit()

# Редактирование
def update_book_year_by_name(book_name, new_year):
    cursor.execute("UPDATE katalog SET god=? WHERE name_knigi=?", (new_year, book_name))
    conn.commit()

def update_books_genre_by_author_and_country(author, country, new_genre):
    cursor.execute("UPDATE katalog SET genre=? WHERE author=? AND country=?", (new_genre, author, country))
    conn.commit()

def update_books_annotation_by_genre(genre, new_annotation):
    cursor.execute("UPDATE katalog SET annotation=? WHERE genre=?", (new_annotation, genre))
    conn.commit()








# Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
# источников в библиотеке. БД должна содержать таблицу Каталог с информацией о
# книгах и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
# Название книги, Год выпуска, Аннотация.

import sqlite3 as sq

conn = sq.connect('library.db')
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

with sq.connect('library.db') as con:
    cursor.executemany("INSERT INTO katalog VALUES (?, ?, ?, ?, ?, ?, ?, ?)", knigi)


def getkniga():
    cursor.execute('SELECT * FROM katalog')
    return cursor.fetchall()


for knigi in getkniga():
    print(knigi)

with sq.connect('library.db') as con:
    cursor.execute("SELECT * FROM katalog WHERE god = 1844")
    result = cursor.fetchall()
    print(result)

with sq.connect('library.db') as con:
    cursor.execute("SELECT * FROM katalog WHERE author='Брэм Стокер' AND country='Ирландия'")
    result = cursor.fetchall()
    print(result)

with sq.connect('library.db') as con:
    cursor.execute("SELECT * FROM katalog WHERE genre='Фантастика'")
    result = cursor.fetchall()
    print(result)

with sq.connect('library.db') as con:
    cursor.execute("DELETE FROM katalog WHERE name_knigi='Властелин колец'")
    result = cursor.fetchall()
    print(result)

with sq.connect('library.db') as con:
    cursor.execute("DELETE FROM katalog WHERE author='Брэм Стокер' AND country='Ирландия'")
    result = cursor.fetchall()
    print(result)

with sq.connect('library.db') as con:
    cursor.execute("DELETE FROM katalog WHERE genre='Детектив'")
    result = cursor.fetchall()
    print(result)


with sq.connect('library.db') as con:
    cursor.execute("UPDATE katalog SET god=? WHERE name_knigi=?", ('1970', 'Хромая судьба'))
    result = cursor.fetchall()
    print(result)

with sq.connect('library.db') as con:
    cursor.execute("UPDATE katalog SET genre='Роман' WHERE author='Джордж Р. Р. Мартин' AND country='Великобритания' ")
    result = cursor.fetchall()
    print(result)

with sq.connect('library.db') as con:
    cursor.execute("UPDATE katalog SET annotation='Том Сойер - весёлый мальчишка из американского городка на Миссисипи' WHERE name_knigi='Приключения Тома Сойера'")
    result = cursor.fetchall()
    print(result)

for knigi in getkniga():
    print(knigi)








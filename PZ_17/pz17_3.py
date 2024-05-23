"""перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
вложенных подкаталогов выводить не нужно.
 перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
test1.В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
файлов в папке test.
 перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
консоль. Использовать функцию basename () (os.path.basename()).
 перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
привязанной к нему программе. Использовать функцию os.startfile().
 удалить файл test.txt"""

# 1
import os

folder_path = r"C:\Users\Yana\Documents\vedenova is-22\PZ 11"

os.chdir(folder_path)

files = os.listdir()

print("\nCписок всех файлов в каталоге PZ11:")
for file in files:
    if os.path.isfile(os.path.join(folder_path, file)):
        print(file)


# 2

"""os.chdir("..")
os.makedirs("test/test1")"""

# os.replace(r"C:\Users\Yana\Documents\vedenova is-22\PZ 6\PZ6_1.py", r"C:\Users\Yana\Documents\vedenova is-22\test\PZ6_1.py")
# os.replace(r"C:\Users\Yana\Documents\vedenova is-22\PZ 6\PZ6_2.py", r"C:\Users\Yana\Documents\vedenova is-22\test\PZ6_2.py")
# os.replace(r"C:\Users\Yana\Documents\vedenova is-22\PZ 7\PZ7_1.py", r"C:\Users\Yana\Documents\vedenova is-22\test\test1\test.txt")

folder_path = "C:/Users/Yana/Documents/vedenova is-22/test"


files = os.listdir(folder_path)
print('\nРазмеры файлов в папке test:')

for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        print(f"File: {file} | Size: {file_size} bytes")

# 3

os.chdir("C:/Users/Yana/Documents/vedenova is-22/PZ 11")
files = os.listdir()
shortest_file = min(files, key=len)
shortest_file_name = os.path.basename(shortest_file)
print(f"\n Файл с самым коротким именем в PZ11: {shortest_file_name}")

# 4

folder_path = "C:/Users/Yana/Documents/vedenova is-22/reports"
os.chdir(folder_path)
os.startfile("C:/Users/Yana/Documents/vedenova is-22/reports/PZ_2.pdf")

# 5

file_path = "C:/Users/Yana/Documents/vedenova is-22/test/test1/test.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File not found.")
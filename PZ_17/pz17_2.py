"""Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9."""

import tkinter as tk
from tkinter import ttk

def display_letters():
    try:
        n = int(entry.get())
        if 1 < n < 26:
            letters = [chr(i + 65) for i in range(n)]
            result_label.config(text="Первые {} буквы алфавита: {}".format(n, ", ".join(letters)))
        else:
            result_label.config(text="Число N должно быть в диапазоне (1, 26)")
    except ValueError:
        result_label.config(text="Введите целое число")

root = tk.Tk()
root.title("Вывод первых N букв алфавита")
root.geometry("700x200")  # Установка размера окна

style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))

label = ttk.Label(root, text="Введите число N (1 < N < 26):")
label.pack(pady=10)

entry = ttk.Entry(root, width=5, font=('Arial', 12))
entry.pack(pady=5)

button = ttk.Button(root, text="Вывести буквы", command=display_letters, style='TButton')
button.pack(pady=10)

result_label = ttk.Label(root, text="", style='TLabel')
result_label.pack(pady=10)

root.mainloop()


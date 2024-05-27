"""Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1)."""

import tkinter as tk
from tkinter import ttk


def on_entry_click(event):
    if about_text.get("1.0", "end-1c") == 'Краткая информация о ваших увлечениях':
       about_text.delete("1.0", tk.END)
       about_text.config(fg='black')


def on_focusout(event):
    if about_text.get("1.0", "end-1c") == '':
        about_text.insert("1.0", 'Краткая информация о ваших увлечениях')
        about_text.config(fg='grey')


def confirm():
    name = name_entry.get()
    password = password_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    interests = ", ".join([interests_var[i].get() for i in range(3)])
    country = country_entry.get()
    city = city_entry.get()
    about = about_text.get("1.0", "end-1c")

    confirmation_label.config(text=f"Имя: {name}\nПароль: {password}\nВозраст: {age}\nПол: {gender}\nУвлечения: {interests}\nСтрана: {country}\nГород: {city}\nО себе: {about}", fg="white")


def clear_form():
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    about_text.delete("1.0", tk.END)
    about_text.insert("1.0", "Краткая информация о ваших увлечениях")
    about_text.config(fg='grey')
    for i in range(len(interests_var)):
        interests_var[i].set(0)
    country_var.set(countries[0])
    city_var.set(cities[0])


root = tk.Tk()
root.title("Форма регистрации пользователя")
root.geometry("750x580")

style = ttk.Style()
style.configure('TFrame', background='white')

main_frame = ttk.Frame(root, padding=10, style='TFrame')
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

title_label = ttk.Label(main_frame, text="Форма регистрации пользователя", font=('Arial', 16, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

form_frame = ttk.Frame(main_frame, relief='groove', borderwidth=2, style='TFrame')
form_frame.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky='nsew')

style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), background='white')
style.configure('TEntry', font=('Arial', 12), fieldbackground='grey')
style.configure('TButton', font=('Arial', 12), background='lightblue', foreground='black')
style.configure('TRadiobutton', font=('Arial', 12), background='white')
style.configure('TCheckbutton', font=('Arial', 12), background='white')

name_label = ttk.Label(form_frame, text="Ваше имя:", background='white')
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

name_entry = ttk.Entry(form_frame, width=60, style='TEntry')
name_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="w")

password_label = ttk.Label(form_frame, text="Пароль:", background='white')
password_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

password_entry = ttk.Entry(form_frame, show="*", width=60, style='TEntry')
password_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")

age_label = ttk.Label(form_frame, text="Возраст:", background='white')
age_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

age_entry = ttk.Entry(form_frame, width=60, style='TEntry')
age_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="w")

gender_label = ttk.Label(form_frame, text="Пол:", background='white')
gender_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
gender_var = tk.StringVar()
gender_var.set("Мужской")
male_radio = ttk.Radiobutton(form_frame, text="Мужской", variable=gender_var, value="Мужской", style='TRadiobutton')
female_radio = ttk.Radiobutton(form_frame, text="Женский", variable=gender_var, value="Женский", style='TRadiobutton')
male_radio.grid(row=3, column=1, padx=10, pady=5, sticky="w")
female_radio.grid(row=3, column=2, padx=10, pady=5, sticky="w")

interests_label = ttk.Label(form_frame, text="Ваши увлечения:", background='white')
interests_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
interests_var = [tk.IntVar() for _ in range(3)]
interests = ["Музыка", "Видео", "Рисование"]
[ttk.Checkbutton(form_frame, text=interests[i], variable=interests_var[i], style='TCheckbutton').grid(row=4, column=i+1, padx=10, pady=5, sticky="w") for i in range(len(interests))]

country_label = ttk.Label(form_frame, text="Ваша страна:", background='white')
country_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)
countries = ["Россия", "США", "Германия"]
country_var = tk.StringVar()
country_var.set(countries[0])
country_entry = ttk.Combobox(form_frame, values=countries, textvariable=country_var, style='TCombobox')
country_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

city_label = ttk.Label(form_frame, text="Ваш город:", background='white')
city_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)
cities = ["Москва", "Нью-Йорк", "Берлин"]  # Пример списка городов
city_var = tk.StringVar()
city_var.set(cities[0])
city_entry = ttk.Combobox(form_frame, values=cities, textvariable=city_var, style='TCombobox')
city_entry.grid(row=8, column=1, padx=10, pady=5, sticky="ew")

about_label = ttk.Label(form_frame, text="Кратко о себе:", background='white')
about_label.grid(row=9, column=0, sticky="w", padx=10, pady=5)
about_text = tk.Text(form_frame, font=('Arial', 12), width=40, height=5)
about_text.insert("1.0", "Краткая информация о ваших увлечениях")
about_text.config(fg='grey')
about_text.bind('<FocusIn>', on_entry_click)
about_text.bind('<FocusOut>', on_focusout)
about_text.grid(row=9, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

calculation_label = ttk.Label(form_frame, text="Решите пример, запишите результат в поле ниже:", background='white')
calculation_label.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky="w")

calculation_entry = ttk.Entry(form_frame, width=40, style='TEntry')
calculation_entry.grid(row=12, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

confirm_button = ttk.Button(form_frame, text="Отменить ввод", command=clear_form, style='TButton')
confirm_button.grid(row=13, column=1, padx=10, pady=10, sticky="e")

cancel_button = ttk.Button(form_frame, text="Данные подтверждаю ", command=root.quit, style='TButton')
cancel_button.grid(row=13, column=2, padx=10, pady=10, sticky="w")
confirmation_label = ttk.Label(form_frame, text="", font=('Arial', 12), background='white')
confirmation_label.grid(row=14, column=0, columnspan=2, sticky='nsew')

root.mainloop()

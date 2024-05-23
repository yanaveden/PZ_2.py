import tkinter as tk
from tkinter import ttk

def confirm():
    name = name_entry.get()
    password = password_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    interests = ", ".join([interests_var[i].get() for i in range(3)])
    country = country_entry.get()
    city = city_entry.get()
    about = about_entry.get()

    confirmation_label.config(text=f"Имя: {name}\nПароль: {password}\nВозраст: {age}\nПол: {gender}\nУвлечения: {interests}\nСтрана: {country}\nГород: {city}\nО себе: {about}", fg="white")

root = tk.Tk()
root.title("Форма регистрации пользователя")
root.geometry("650x560")  # Увеличенная ширина окна

style = ttk.Style()
style.configure('TFrame', background='white')  # Установка фона для TFrame

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
name_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

name_entry = ttk.Entry(form_frame, width=50, style='TEntry')
name_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="w")

password_label = ttk.Label(form_frame, text="Пароль:", background='white')
password_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

password_entry = ttk.Entry(form_frame, show="*", width=50, style='TEntry')
password_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")

age_label = ttk.Label(form_frame, text="Возраст:", background='white')
age_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

age_entry = ttk.Entry(form_frame, width=50, style='TEntry')
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
checkboxes = []
for i, interest in enumerate(interests):
    checkbox = ttk.Checkbutton(form_frame, text=interest, variable=interests_var[i], style='TCheckbutton')
    checkbox.grid(row=i+4, column=1, padx=10, pady=5, sticky="w")
    checkboxes.append(checkbox)

country_label = ttk.Label(form_frame, text="Ваша страна:", background='white')
country_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)
countries = ["Россия", "США", "Германия"]  # Пример списка стран
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
about_entry = ttk.Entry(form_frame, font=('Arial', 12), width=40, style='TEntry')
about_entry.insert(0, "Краткая информация о ваших увлечениях")
about_entry.grid(row=9, column=1, columnspan=2, padx=10, pady=5, rowspan=2, sticky="nsew")

calculation_label = ttk.Label(form_frame, text="Решите пример, запишите результат в поле ниже:", background='white')
calculation_label.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky="w")

calculation_entry = ttk.Entry(form_frame, width=40, style='TEntry')
calculation_entry.grid(row=12, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

confirm_button = ttk.Button(form_frame, text="Отменить ввод", command=confirm, style='TButton')
confirm_button.grid(row=13, column=1, padx=10, pady=10, sticky="e")

cancel_button = ttk.Button(form_frame, text="Данные подтверждаю ", command=root.quit, style='TButton')
cancel_button.grid(row=13, column=2, padx=10, pady=10, sticky="w")
confirmation_label = ttk.Label(form_frame, text="", font=('Arial', 12), background='white')
confirmation_label.grid(row=14, column=0, columnspan=2, sticky='nsew')

root.mainloop()

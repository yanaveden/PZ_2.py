"""Для задачи из блока 1 создать две функции, save_def и
load_def, которые позволяют сохранять информацию из экземпляров класса (3
шт.) в файл и загружать ее обратно. Использовать модуль pickle для
сериализации и десериализации объектов Python в бинарном формате."""


import pickle


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_weekday(self):
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        weekday = (self.day + 2 * self.month + 3 * (self.month + 1) // 5 + self.year + self.year // 4 - self.year // 100 + self.year // 400) % 7
        return days[weekday]

    def is_leap_year(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return True
        else:
            return False

    def get_days_in_month(self):
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days = days_in_months[self.month - 1]

        if self.is_leap_year() and self.month == 2:
            days += 1

        return days


def save_def(calendars, filename):
    with open(filename, 'wb') as f:
        pickle.dump(calendars, f)


def load_def(filename):
    with open(filename, 'rb') as f:
        calendars = pickle.load(f)
    return calendars


calendar1 = Calendar(2024, 5, 7)
calendar2 = Calendar(2023, 12, 31)
calendar3 = Calendar(2022, 2, 14)


calendars = [calendar1, calendar2, calendar3]
save_def(calendars, 'calendars.pkl')


loaded_calendars = load_def('calendars.pkl')


for calendar in loaded_calendars:
    print(calendar.get_weekday())
    print(calendar.is_leap_year())
    print(calendar.get_days_in_month())
    print()

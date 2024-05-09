""": Создайте класс «Календарь», который имеет атрибуты
год, месяц и день. Добавьте методы для определения дня недели, проверки на
високосный год и определения количества дней в месяце."""


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


calendar = Calendar(2024, 5, 7)
print(calendar.get_weekday())
print(calendar.is_leap_year())
print(calendar.get_days_in_month())
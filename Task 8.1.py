"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Date:
    int_data = str(input("Введите дату в формате «день-месяц-год»: "))


    @classmethod
    def extract(cls):
        new_date = [int(el) for el in cls.int_data.split() if el != '-']
        cls.day, cls.month, cls.year = new_date

    @staticmethod
    def correct_date():
        if Date.day <= 31:
            if Date.month <= 12:
                if Date.year <= 2022:
                    return f"Дата корректна"
                else:
                    return f"Год введен неверно"
            else:
                return f"Месяц введен неверно"
        else:
            return f"День введен неверно"

Date.extract()
print(Date.correct_date())


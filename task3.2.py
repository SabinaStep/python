"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""

def user_dates(name, surname, birth_date, city, email, number):
    print(f"имя - {name}; фамилия - {surname}; год рождения - {birth_date}; "
          f"город проживания - {city}; email - {email}; телефон - {number}")
user_dates(name="Анна", email="anna@ya.ru", number="486765", surname="Иванова",
           birth_date="15.06.1991", city="Лондон")

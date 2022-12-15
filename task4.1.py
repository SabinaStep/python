"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
заработной платы сотрудника. Используйте в нём формулу:
(выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_salary, hours_1, hour_cost_1, bonus_1 = argv

def count_salary(hours, hour_cost, bonus):
    return (int(hours) * int(hour_cost) + int(bonus))

#count_salary(hours_1, hour_cost_1, bonus_1)
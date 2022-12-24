"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivisionError(Exception):
    def __init__(self, data):
        self.data = data


def count(numb1, numb2):
    try:
        if numb2 == 0:
            raise ZeroDivisionError ("На 0 делить нельзя")
        print(numb1 / numb2)
    except ZeroDivisionError as err:
        print(err)

count(22, 0)
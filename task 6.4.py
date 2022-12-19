"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print ('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn_direction(self):
        print('Машина повернула')

    def show_speed(self):
        return f'скорость машины {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'скорость машины превышена {self.speed}'
        else:
            return f'скорость машины {self.speed}'

TC_obj = TownCar (70, 'red','ford')
print(TC_obj.show_speed())
c_obj = Car (55, 'black','mazda')
print(c_obj.show_speed())
c_obj.turn_direction()

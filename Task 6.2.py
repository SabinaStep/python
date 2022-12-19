"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""

class Road:
    wight_road = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_road_total(self):
        weight_road_total = self._length * self._width * self.wight_road * self.thickness
        print(f'Для {self._length} метров дороги требуется {weight_road_total} кг. асфальта ')

road_obj = Road(5000, 20)
road_obj.weight_road_total()


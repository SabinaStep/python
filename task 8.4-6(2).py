"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в
определённое подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру (например, словарь).
"""

class Stock:
    stock = {}

    def income_order(self, company_name, equip):
        if company_name in self.stock:
            self.stock[company_name].append(equip)
        else:
            self.stock[company_name] = []
            self.stock[company_name].append(equip)
        

class OfficeEquipment:
    def __init__(self, name, producer, price):
        self.name = name
        self.producer = producer

        if (self.correct(price)): 
            self.price = price
        else:
            print('Ввели не число. Цена не записана')
    
    def __str__(self):
        return f'{self.name}, {self.producer}, {self.price}'

    def correct(self, price):
        if type(price) == int:
            return True
        else:
            return False
    
    def information(self):
        return f"Дополнительная информация о принтере\n---\nИмя:\t{self.name}\nПроиз.:\t{self.producer}\nЦена:\t{self.price}"


class Printer(OfficeEquipment):
    print_speed = 40

class Scanner(OfficeEquipment):
    dualside_scan = True

    

class Xerox(OfficeEquipment):
    xerox_speed = 20

s = Stock()
p = Scanner("Scanner","Asus", 12)

s.income_order('R&D', p)
print(s.stock)
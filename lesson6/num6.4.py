"""
3. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        return f'машина повернула {direction}'

    def show_speed(self):
        return f"Скорость авто {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            return "Привышение скорости"
        else:
            return f"Скорость авто {self.speed}"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            return "Привышение скорости"
        else:
            return f"Скорость авто {self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)


bmv = WorkCar(100, "blue", "name")
print(bmv.show_speed())
print(bmv.go())
print(bmv.stop())
print(bmv.turn("Вправо"))
"""
Привышение скорости
Машина поехала
Машина остановилась
машина повернула Вправо
"""
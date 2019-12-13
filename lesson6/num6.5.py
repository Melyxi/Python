"""
4. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш),Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Ручка"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Карандаш"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "маркер"


r = Stationery("Рисунок")
print(r.title)
hand = Handle("заголовок")
print(hand.draw())

pen = Pencil("sdfkds")
print(pen.title, pen.draw())

"""
Рисунок
маркер
sdfkds Карандаш
"""
"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count
from itertools import cycle


def itter(start):
    while True:
        for el in count(start):
            yield el


def my_cycle(list_el):
    while True:
        for el in cycle(list_el):
            yield el


for el in itter(90):
    print(el)

for el in my_cycle([1, 2, 3, 4]):
    print(el)
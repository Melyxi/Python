"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

list_a = [1, "string", 3.456, None, 1+2j, [3, 5, "type", 6, 7], (1, "5", 6, 2), {1, 3, "43", 7, 8}, {1: "один"}, True, int]

for itm in list_a:
    print(type(itm))

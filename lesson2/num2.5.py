"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]

num = int(input("Введите новый элемент: "))

my_list.append(num) # добавляем в список
my_list = sorted(my_list, reverse=True) # сортируем его на убывание

print(my_list)

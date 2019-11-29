"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(var1, var2, var3):
    list_var = [var1, var2, var3]
    list_var = sorted(list_var)
    return list_var[-1] + list_var[-2]


my_func(2, 4, 5)

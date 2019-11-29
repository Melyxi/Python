"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_f(var1, var2):
    while True:
        try:
            var3 = int(input("Введите число"))
            break
        except ValueError:
            print("Введите число")

    try:
        var4 = var1 / var3
        var5 = var2 / var3
        return var4, var5
    except ZeroDivisionError:
        return "Делить на ноль нельзя"


print(my_f(int(input("1 число")), int(input("2 число"))))

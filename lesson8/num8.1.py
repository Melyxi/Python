"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Error(Exception):
    def __init__(self, message: str):
        self.message = message
        Exception.__init__(self)  # зачем эта строчка?

    def __str__(self):
        return self.message


class Date:
    @classmethod
    def to_int(cls, str_date: str):
        return tuple(map(int, str_date.split("-")))

    @staticmethod
    def valid(str_date):
        list_date = list(Date.to_int(str_date))
        if 0 < list_date[1] < 12 and 0 < list_date[2]:

            return Date.to_int(str_date)
        else:
            raise Error("неверный месяц или год")


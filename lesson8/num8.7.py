"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyComplex:
    def __init__(self, re=0, lm=0):
        self.re = re
        self.lm = lm

    def __str__(self):
        if self.lm == 0 or self.re == 0:
            if self.re == 0:
                return str(self.lm) + 'i'
            else:
                return str(self.re)
        else:
            return f"{self.re}" + ('+' if self.lm > 0 else "") + f"{self.lm}i"

    def __mul__(self, other):
        return MyComplex((self.re * other.re + self.lm * other.lm * (-1)), (self.lm * other.re + self.re * other.lm))

    def __add__(self, other):
        return MyComplex((self.re + other.re), (self.lm + other.lm))

    def __sub__(self, other):
        return MyComplex((self.re - other.re), (self.lm - other.lm))
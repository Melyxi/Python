"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

import os

# path = os.getcwd()
name = "text_finance.txt"

with open(os.path.join(os.getcwd(), name), 'r') as file:
    summ = 0
    col = 0
    for line in file:
        # print(line)

        try:
            # print(line.split()[1])
            money = float(line.split()[1])
            summ += money
            col += 1
            if money < 20000:
                print(line.split()[0])

        except ValueError:
            continue

        except IndexError:
            continue

print("среднее", '{:.4f}'.format(summ / col))

"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import os
import json


def firm_write(list_line):
    firm_dict = {}
    average_profit = {}
    profit_list = []
    total_list = []
    # print(profit_list)
    for line in list_line:
        list_str = line.split()
        # print(list_str)
        profit = float(list_str[2]) - float(list_str[3])

        if profit > 0:
            profit_list.append(profit)
        firm_dict[list_str[0]] = profit

    total_list.append(firm_dict)

    if len(profit_list) > 0:
        average_profit["average_profit"] = sum(profit_list) / len(profit_list)
        total_list.append(average_profit)

    return total_list


# path = os.getcwd()
name = "firm.txt"
name_json = 'firm.json'

with open(os.path.join(os.getcwd(), name), 'r') as file:
    list_line = file.readlines()  # считываем файл

# print(list_line)

data = firm_write(list_line)

with open(os.path.join(os.getcwd(), name_json), "w") as file:
    json.dump(data, file)

print(firm_write(list_line))

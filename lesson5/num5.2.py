"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""

import os


# path = os.getcwd()
name = "text_string.txt"


with open(os.path.join(os.getcwd(), name), 'r') as file:
    sum_str = 0
    for indx, line in enumerate(file, 1):
        sum_str += 1
        print(f'в {indx} строке: {len(line.split())}')
        #print(line)
print('всего строк:', sum_str)

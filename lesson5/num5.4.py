"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os


def rus_number(list_str, new_name):  # функция для записи новых строк
    with open(os.path.join(os.getcwd(), new_name), 'w') as file:
        for line in list_str:
            file.write(line)
            file.write("\n")


# path = os.getcwd()
name = "eng_num.txt"
new_name = "rus_num.txt"

rus_num = {'One': "Один", 'Two': "Два", 'Three': "Три", 'Four': "Четыре"}

with open(os.path.join(os.getcwd(), name), 'r') as file:
    list_str = []
    for line in file:
        # print(line)

        try:
            list_word = line.split()
            list_word[0] = rus_num[list_word[0]]
            new_str = ' '.join(list_word)
            list_str.append(new_str)


        except KeyError:  # на случай, если нет такого ключа
            continue  # как объеденить ecxept?

        except IndexError:  # на случай если есть пустые строки
            continue

rus_number(list_str, new_name)

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os

# path = os.getcwd()
name = "summ_num.txt"

with open(os.path.join(os.getcwd(), name), 'w') as file:
    str_num = input("Введите числа: ")
    file.write(str_num)

with open(os.path.join(os.getcwd(), name), 'r') as file:
    read_str = file.readline()

    summ = 0
    for num in read_str.split():

        try:  # на случай если это не число
            summ += float(num)
        except:
            continue

print(summ)

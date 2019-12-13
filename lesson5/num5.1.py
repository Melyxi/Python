"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import os

# path = os.getcwd()
name = "text.txt"

with open(os.path.join(os.getcwd(), name), 'w') as file:
    string = True
    while string:
        string = input("Введите строку")
        file.write(string + '\n')

with open(os.path.join(os.getcwd(), name), 'r') as file:
    print(file.read())

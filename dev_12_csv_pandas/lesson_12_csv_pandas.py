import random

import pandas

# print(random.choice([1,2,3])) # случайное число из представленной последовательности: список, кортеж, диапазон
# print(*(i for i in range(4))) # оператор * отвечает за распаковку списка, кортежа, множества, строк.да
# ** - данный оператор отвечает за распаковку словарей

# x = 1
# y = 2
# c = 3
# numbers = x, y, c
# print(*numbers)

# x = [1,2,3]
# print(reversed(x) == x[::-1]) # False потому что два разных класса

# a = sorted([1,2,3,4,5])
# b = [1,2,3,4,5].sort()
# print(a == b)

# csv файл

"""
Имя; Пол; Возраст
Петя; муж.; 20
Алина; жен.; 21
"""

# data = [
#     ['Имя', 'Пол', 'Возраст'],
#     ['Петя', 'муж.', '20',],
#     ['Алина', 'жен.', '21']
# ]
# csv = ''
# for row in data:
#     csv += ';'.join(row) + '\n'
# print(csv)

# запись в csv
import csv
# name = 'Petya'
# with open('example.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(name)

# запись строк
# name = 'Petya'
# name2 = 'Miwa'
# with open('example.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([name, name2])

# запись заголовка таблицы
# with open('example.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(
#         ('login', 'password')
#     )

# data = [
#     ['login1', 'password1'],
#     ['login1', 'password1'],
#     ['login1', 'password1']
# ]
# for elem in data:
#     with open('example.csv', 'a') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(elem)

# with open('example.csv', 'a', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(data)

# writerow - записывает по строчно
# writerows - записывает весь список сразу

# lines = [
#     {'name':'Petya', 'age':20, 'sex':'m'},
#     {'name':'Миша', 'age':25, 'sex':'m'},
# ]
# with open('example.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['age', 'sex', 'name'], delimiter=';')
#     writer.writerows(lines)

# чтение из файла

# with open('example.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=';')
#     for elem in reader:
#         print(elem)


# Pandas для csv на запись и чтение
# import pandas
# data = pandas.read_csv('example.csv')
# print(data)
# lines = [
#     {'name':'Petya', 'age':20, 'sex':'m'},
#     {'name':'Miwa', 'age':25, 'sex':'m'},
#     ]
# lines2 = [
#     ['name', 'sex', 'age'],
#     ['Petya', 'm.', '20',],
#     ['Alina', 'j.', '21'],
# ]
#
# lines = pandas.DataFrame(lines)
# lines2 = pandas.DataFrame(lines2)
#
# lines.to_csv('example.csv', index=False)
# lines2.to_csv('example2.csv', index=False)

# Напишите программу, которая запрашивает у пользователя данные о студентах и сохраняет их в файл формата CSV.
# Требования:
# Программа должна запрашивать у пользователя информацию о каждом студенте, включая имя, фамилию и возраст.
# Информация о каждом студенте должна быть сохранена в отдельной строке файла CSV.
# Файл CSV должен иметь следующие заголовки столбцов: "Имя", "Фамилия", "Возраст".
# Программа должна продолжать запрашивать информацию о студентах до тех пор, пока пользователь не введет команду
# "stop" для завершения.
# В конце выполнения программы должно быть выведено сообщение о успешном сохранении данных.
# a = input('Введите номер класса: ')
# name = 1
# full_name = 1
# age = 1
# with open(a + '.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(
#         ('name', 'full_name', 'age')
#     )
# lines = {}
# while name and full_name and age:
#     lines['name'] = input('Введите имя ')
#     if lines['name'] == 'STOP':
#         break
#     lines['full_name'] = input('Введите Фамилию ')
#     lines['age'] = input('Введите возраст ')
#     with open(a+'.csv', 'a', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=['name', 'full_name', 'age'], delimiter=';')
#         writer.writerow(lines)
#
# print('Данные успешно записаны!')

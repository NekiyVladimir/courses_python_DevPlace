# 1. Напишите программу, которая запрашивает у пользователя данные о студентах и сохраняет их в файл формата
# CSV. Требования: Программа должна запрашивать у пользователя информацию о каждом студенте, включая имя, фамилию
# и возраст. Информация о каждом студенте должна быть сохранена в отдельной строке файла CSV. Файл CSV должен иметь
# следующие заголовки столбцов: "Имя", "Фамилия", "Возраст". Программа должна продолжать запрашивать информацию о
# студентах до тех пор, пока пользователь не введет команду "stop" для завершения. В конце выполнения программы должно
# быть выведено сообщение о успешном сохранении данных.(кто не дорешал)

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


# 2. Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее
# содержимое, как и всех подкаталогов(вывести имя папки и имена файлов)

# import os
# for dirpath, dirnames, filenames in os.walk('/Users/Vladimir/Test'):
#     # перебрать каталоги
#     for dirname in dirnames:
#         print("Каталог:",  dirname)
#     # перебрать файлы
#     for filename in filenames:
#         print("Файл:", dirname,'/',filename)

# 3. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов,
# если таковых несколько).

# with open('article.txt', 'r', encoding='utf-8') as file:
#     list1 = []
#
#     while True:
#         a = file.readline().strip()
#         if not a:
#             break
#         list1 += a.split()
#     def longest_words(prem):
#         b = 'a'
#         c = 'a'
#         for i in prem:
#             if len(i) == len(b):
#                 c = c + ' '
#                 c = c + i
#                 b = i
#             elif len(i) > len(b):
#                 c = b = i
#         return c
# print(longest_words(list1))

# 4. Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью
# символа табуляции \t разделена на три колонки: наименование товара; количество товара (целое число); цена (в рублях)
# товара за 1 шт. (целое число). Напишите программу, подсчитывающую общую стоимость заказа.

# with open('price.txt', 'r', encoding='utf-8') as file:
#     list1 = []
#     number = 0
#     print('Чек')
#     print('Наименование - Кол-во - Цена за 1 шт.')
#     while True:
#         a = file.readline().split()
#         if not a:
#             break
#         print(f'{a[0]} - {a[1]} - {a[2]}')
#         number = int(a[1]) * int(a[2])
#         list1.append(number)
# print(f'Общая стоимость товаров в чеке составляет {sum(list1)} руб.')

# 5. Вам предоставляется CSV-файл, содержащий данные о продажах различных товаров. Каждая строка файла содержит
# информацию о конкретной продаже: название товара, количество проданных единиц и цена за единицу. Ваша
# задача - написать программу, которая считывает данные из файла и вычисляет общую сумму продаж.

# import csv
# with open('price.csv', 'r', encoding='utf-8') as file:
#     file_reader = csv.reader(file, delimiter=",")
#     summa = 0
#     for row in file_reader:
#         print(f'Товар {row[0]} обошолся {int(row[1]) * int(row[2])} руб.')
#         summa = summa + (int(row[1])*int(row[2]))
# print(f'Общая сумма за товар составила {summa} руб.')
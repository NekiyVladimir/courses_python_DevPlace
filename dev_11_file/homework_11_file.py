# 1. Файл содержит числа и буквы. Каждый записан в отдельной строке. Нужно считать содержимое в список так, чтобы
# сначала шли числа по возрастанию, а потом слова по возрастанию их длины.

# file1 = open("hw_task1.txt", 'r')
# list1 = []
# list2 = []
# def is_int(str):
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False
#
# while True:
#     line = file1.readline().strip()
#     if is_int(line):
#         list1.append(int(line))
#         list1.sort()
#     else:
#         list2.append(line)
#         list2.sort(key=len)
#
#     if not line:
#         break
#
# file1.close
# list2.pop(0)
# print(list1+list2)

# 2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

# file1 = open("hw_task2.txt", 'w')
# a = True
# while a:
#     a = input('Введите вводные данные: ')
#     if a:
#         file1.write(a + '\n')
#     else:
#         break
#
# print('Конец программы')
# file1.close

# 3. В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество
# в ней символов.

# file1 = open("hw_task2.txt", 'r')
# summ1 = 0
# while True:
#     line = file1.readline().strip()
#     summ1 += 1
#     print(f'Длина строки {line} составляет {len(line)} символов!')
#     if not line:
#         break
# print('Общее количество строк в файле: ' + str(summ1))
# file1.close

# 4. Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом, то должна
# выполняться конкатенация, то есть соединение, строк. В остальных случаях введенные числа суммируются.
# a = b = 1
#
# while a or b:
#     a = input('Введите первый элемент: ')
#     b = input('Введите второй элемент: ')
#     if a.isdigit() and b.isdigit():
#         print(f'Ответ: {int(a) + int(b)}')
#     else:
#         print(f'Ответ: {a + " " + b}')
# print('Конец программы!')
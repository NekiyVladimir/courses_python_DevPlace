# 1) Проверить, есть ли у последовательности дубликаты?
# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
# a = 'pythonist'
# if len(set(a)) == len(list(a)):
#     print('Дубликатов нет')
# else:
#     print(('дубликаты есть'))
#
# dct = {}
# for i in range(1,10):
#     dct[i] = i**3
# print(dct)


# 2) Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами. Выведите полученный словарь на экран.

# a = [1,2,3]
# b = [0,0,0]
# d1 = dict(zip(a,b))
# d2 = {}
# print(f'Первый способ: {d1}')
# for i in range(1,4):
#     d2[i] = b[i-1]
# print(f'Второй способ: {d2}')
# d3 = dict.fromkeys(a, 0)
# print(f'Третий способ: {d3}')

#4) Создать произвольный словарь 2. Добавить новый элемент с ключом типа str и значением типа int 3. Добавить
# новый элемент с ключом типа кортеж(tuple) и значением типа список(list) 4. Получить элемент по ключу 5. Удалить
# элемент по ключу 6. Получить список ключей словаря.

# d = {'1': 0, '2': 0, '3': 0}
# d['four'] = 4
# print(d)
# d[(1,2,3)] = [3,2,1]
# print(d)
# print(d['1'])
# d.pop((1,2,3))
# print(d)
# print(d.keys())

# 5) Создать множество. Создать неизменяемое множество. Выполнить операцию объединения созданных множеств.
# Выполнить операцию пересечения созданных множеств.

# a1 = 'pythonist'
# a2 = 'hello'
# b = set(a1)
# c = frozenset(a2)
# print(b)
# print(c)
# d = b | c
# print(d)
# print(b.intersection(c))

# 6) Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры.

# n = int(input('Введите число: '))
# name = input('Введите имя ')
# email = input('Введите почту ')
# dct = {'name': name, 'email': email}
# a = {k:dct for k in range(1,n)}
# print(a)

# 7) Даны списки:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(list(set(a).intersection(set(b))))


# 8) Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково
# читаются слева направо и справа налево.

# a = input('Введите слово ')
# if list(a) == list(a[::-1]):
#     print('Полиндром')
# else:
#     print('Не полиндром')


# 9)  В списке целых чисел с количеством элементов 19 определить максимальное число и заменить им все четные
# по значению элементы.

# from random import randint
# lst = [randint(0, 100) for i in range(20)]
# print(lst)
# number = max(lst)
# for i in lst:
#     if i % 2 == 0:
#         lst[lst.index(i)] = number
# print(lst)



# 10) Даны два кортежа:
#
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
#
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1. Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..)
# 2. Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей

# c_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# c_2 = (45, 21,124,76,5,23,91,234)
# if sum(c_1) > sum(c_2):
#     print(f'Сумма больше в кортеже - c_1 = {c_1}')
# elif sum(c_1) < sum(c_2):
#     print(f'Сумма больше в кортеже - C_2 = {c_2}')
# else:
#     print(f'Суммы элементов кортежей равны')
# print(f'Порядковый номер минимального элемента в кортеже с_1 - {c_1.index(min(c_1))+1}')
# print(f'Порядковый номер максимального элемента в кортеже с_1 - {c_1.index(max(c_1))+1}')
# print(f'Порядковый номер минимального элемента в кортеже с_2 - {c_2.index(min(c_2))+1}')
# print(f'Порядковый номер максимального элемента в кортеже с_2 - {c_2.index(max(c_2))+1}')

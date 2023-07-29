# Николай знает, что кортежи являются неизменяемыми, но он с этим не готов соглашаться. Ученик решил создать функцию
# del_from_tuple(), которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать
# кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. К слову, Николай
# не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).
import random


# def del_from_tuple(a, b):
#     if b not in a:
#         return a
#     else:
#         a = list(a)
#         a.pop(a.index(b))
#         return tuple(a)
#
# print(del_from_tuple((1,2,3,4,5,6), 2))

# Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).
# Примеры:
# likes() -> "no one likes this"
# likes("Ann") -> "Ann likes this"
# likes("Ann", "Alex") -> "Ann and Alex like this"
# likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
# likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"

# likes = ['Anna', 'Beta', 'Masha', 'Gamma']
# def quantity_likes(likes):
#     if len(likes) == 0:
#         return 'no one likes this'
#     elif len(likes) == 1:
#         return f'{likes[0]} likes this'
#     elif len(likes) == 2:
#         return f'{likes[0]} and {likes[1]} like this'
#     elif len(likes) == 3:
#         return f'{likes[0]}, {likes[1]} and {likes[2]} like this'
#     else:
#         return f'{likes[0]}, {likes[1]} and {len(likes)-2} others like this'
#
# print(quantity_likes(likes))


# Написать функцию, которая определяет количество разрядов введенного целого числа.

# def numbers(n):
#     a = list(str(n))[::-1]
#     b = [a[i:i+3] for i in range(0, len(a), 3)]
#     for i in b[::-1]:
#         print(''.join(i), end=' ')
#
# numbers(123456789777)

# В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или треугольника. Для вычисления
# площади каждой фигуры должна быть написана отдельная функция.


#
# def var1():
#     import math
#     param = float(input('Введите радиус круга: '))
#     b = 2 * param * math.pi
#     return b
#
# def var2():
#     param1 = float(input('Введите длину первой стороны: '))
#     param2 = float(input('Введите длину второй стороны: '))
#     param3 = float(input('Введите длину третьей стороны: '))
#     b = param1 + param2 + param3
#     return b
#
# def var3():
#     param1 = float(input('Введите длину первой стороны: '))
#     param2 = float(input('Введите длину второй стороны: '))
#     b = (param1+param2) * 2
#     return b
#
# while True:
#     a = input('Выберите фигуру (треугольник, круг, прямоугольник) для осуществления вычислительных операций: ')
#
#     if a == 'треугольник':
#         print(var2())
#     elif a == 'круг':
#         print(var1())
#     elif a == 'прямоуголник':
#         print(var3())
#     elif a != True:
#         print('Конец программы!')
#         break
#     else:
#         print('Сделайте выбор из предложенных вариантов!')

# Написать функцию, которая заполняет массив длинной 10 элементов, случайными числами в диапазоне, указанном
# пользователем с клавиатуры. Функция должна принимать два аргумента – начало диапазона и его конец, при этом ничего
# не возвращать.

# def list1(a,b):
#     import random
#     global result
#     result = [random.randint(a,b) for i in range(10)]
#
#
# a = int(input('Введите число начало диапазона: '))
# b = int(input('Введите число конец диапазона: '))
#
# list1(a,b)
# print(result)

# Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

# def time(a):
#     day = a // 86400
#     hour = (a - (day*86400)) // 3600
#     minutes = (a - (day*86400) - (hour *3600)) // 60
#     seconds = a % 60
#     return "%02d:%02d:%02d:%02d" % (day, hour, minutes, seconds)
#
# print(time(100000))

# Написать функцию, которая считает сколько гласных и согласных в строке. Строку вводить с клавиатуры.

# def string(a):
#     sumglass = 0
#     sumsoglass = 0
#     words = ['a','e','i','o','u']
#     for i in a:
#         if i in words:
#             sumglass += 1
#         else:
#             sumsoglass += 1
#     print(f'Согласных букв: {sumsoglass}, гласных букв: {sumglass}.')
#
# a = input('Введите строку: ')
# string(a)

# Функцию, которая при заданном целом числе n посчитает n + nn + nnn.
# n = str(input('Введите целое число: '))
# def numbers(n):
#     summa = 0
#     a =[n*i for i in range(1, 4)]
#     for i in a:
#         summa += int(i)
#     return summa
#
# print(numbers(n))

# Если в функцию передаётся кортеж, то посчитать длину всех его слов. Если список, то посчитать кол-во букв и чисел
# в нём. Число – кол-во нечётных цифр. Строка – кол-во букв. Сделать проверку со всеми этими случаями.

# def func(a):
#     summa = 0
#     numbers = 0
#     if type(a) == type(tuple()):
#         for i in a:
#             summa += len(str(i))
#         return 'Длина всех слов коретжа равна: ' + str(summa)
#     elif type(a) == type([]):
#         for i in a:
#             if type(i) == type(str()):
#                 summa += len(i)
#             elif type(i) == type(int()):
#                 numbers += 1
#         return 'Количество всех букв равно: ' + str(summa) + ' Количество всех чисел равно: ' + str(numbers)
#         'Количество всех чисел равно: ' + str(numbers)
#     elif type(a) == type(int()):
#         for i in range(0,len(str(a))):
#             a = str(a)
#             if int(a[i]) % 2 == 1:
#                 summa += 1
#         return 'Количество нечетных цифр равно: ' + str(summa)
#     elif type(a) == type(str()):
#         return 'Количество букв: ' + str(len(a))

# Функция sum(a,b) принимает 2 числа и возвращает их сумму. Написать декоратор, который возвращает ошибку если
# переданы не числовые параметры(например строка)
# def validate_int_parameters(func):
#     def number(n,m):
#         if type('help') == type(n) or type('help') == type(m):
#             print('Ошибка')
#         func(n,m)
#     return number
#
# @validate_int_parameters
# def sum(a,b):
#     if type(a) == type(b) == type(1):
#         print(a+b)
#
# sum(2,5)



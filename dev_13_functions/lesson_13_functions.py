# Декораторы

# def decorator(func):
#     def wrapper():
#         print('start function')
#         func()
#         print('stop function')
#     return wrapper
#
# @decorator
# def first_func():
#     print('first_func')
#
# @decorator
# def second_func():
#     print('second_func')
#
#
# first_func()
# second_func()

# 1) Написать функцию is_year_leap, принимающую 1 аргумент —год, и возвращающую True, если год високосный,
# и False иначе.

# def is_year_leap(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False
#
# year = int(input('Введите год: '))
# print(is_year_leap(year))

# 2) Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата. Сторону квадрата вводить с клавиатуры.

# import math
# def square(x):
#     a = (x*4), (x**2), (x*(math.sqrt(2)))
#     return a
#
# x = int(input('Число: '))
# print(square(x))

# 3) Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень). Номер месяца вводить с клавиатуры.

# def season(x):
#     if x in [12,1,2]:
#         return 'Зима'
#     elif x in [3,4,5]:
#         return 'Весна'
#     elif x in [6,7,8]:
#         return 'Лето'
#     else:
#         return 'Осень'
#
# x = int(input('Введите вичсло от 1 до 12: '))
# print(season(x))

# 4) Функция, вычисляющая среднее арифметическое элементов списка. Список должен состоять из случайных чисел,
# длинной 10 элементов.

# def number(x):
#     return sum(x)/len(x)
#
# print(number(x=[i for i in range(1,11)]))

# 5) Создайте функцию, добавьте в неё локальное значение. Сделайте так, чтобы другая функция принимала это значение в
# качестве параметра.

def func1():
    global x
    x = 1
    return x

def func2(x):
    return x

print(func1())
print(func2(x))
























